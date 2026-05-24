"""
自动化任务模块
包含周易推送和古诗推送功能
"""

import json
import os
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dataclasses import dataclass
from config import config
from main import MiMoClient

def push_to_pushplus(title: str, content: str) -> bool:
    """推送内容到微信（通过 PushPlus）"""
    if not config.pushplus_token:
        print("警告: PUSHPLUS_TOKEN 未设置")
        return False
    
    url = "http://www.pushplus.plus/send"
    data = {
        "token": config.pushplus_token,
        "title": title,
        "content": content,
        "template": "markdown"
    }
    
    try:
        response = requests.post(url, json=data, timeout=30)
        result = response.json()
        if result.get("code") == 200:
            print(f"PushPlus 推送成功: {title}")
            return True
        else:
            print(f"PushPlus 推送失败: {result.get('msg', '未知错误')}")
            return False
    except Exception as e:
        print(f"PushPlus 推送异常: {e}")
        return False

@dataclass
class AutomationTask:
    """自动化任务基类"""
    name: str
    description: str
    schedule: str  # cron 表达式或描述
    enabled: bool = True
    
    def run(self):
        """运行任务"""
        raise NotImplementedError

class ZhouyiPushTask(AutomationTask):
    """周易推送任务"""
    
    def __init__(self):
        super().__init__(
            name="每日周易推送",
            description="每天推送一章周易内容，包括卦名、卦辞、爻辞和简要解释",
            schedule=f"每天 {config.zhouyi_push_hour}:{config.zhouyi_push_minute:02d}"
        )
        self.client = MiMoClient()
        self.data_file = os.path.join(config.data_dir, "zhouyi_progress.json")
        self.load_progress()
    
    def load_progress(self):
        """加载进度"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.current_hexagram = data.get("current_hexagram", 1)
            else:
                self.current_hexagram = 1
        except Exception:
            self.current_hexagram = 1
    
    def save_progress(self):
        """保存进度"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump({"current_hexagram": self.current_hexagram}, f)
    
    def run(self):
        """运行周易推送"""
        if not config.validate():
            return "配置验证失败"
        
        # 64卦列表
        hexagrams = [
            "乾", "坤", "屯", "蒙", "需", "讼", "师", "比",
            "小畜", "履", "泰", "否", "同人", "大有", "谦", "豫",
            "随", "蛊", "临", "观", "噬嗑", "贲", "剥", "复",
            "无妄", "大畜", "颐", "大过", "坎", "离", "咸", "恒",
            "遁", "大壮", "晋", "明夷", "家人", "睽", "蹇", "解",
            "损", "益", "夬", "姤", "萃", "升", "困", "井",
            "革", "鼎", "震", "艮", "渐", "归妹", "丰", "旅",
            "巽", "兑", "涣", "节", "中孚", "小过", "既济", "未济"
        ]
        
        if self.current_hexagram > 64:
            self.current_hexagram = 1
        
        hexagram_name = hexagrams[self.current_hexagram - 1]
        
        # 使用 MiMo API 生成内容
        prompt = f"""
请生成周易第{self.current_hexagram}卦{hexagram_name}卦的详细内容，包括：
1. 卦名和卦象
2. 卦辞（原文和白话解释）
3. 六爻爻辞（原文和白话解释）
4. 整体简要解释
5. 现代应用建议

请用清晰、易懂的格式输出，适合每日学习。
"""
        
        try:
            response = self.client.chat(
                messages=[{"role": "user", "content": prompt}],
                model="mimo-v2.5-pro",
                temperature=0.7,
                max_completion_tokens=2000
            )
            
            if "error" in response:
                return f"生成内容失败: {response['error']}"
            
            content = response.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            # 更新进度
            self.current_hexagram += 1
            self.save_progress()
            
            # 根据推送方式处理
            title = f"每日周易推送 - 第{self.current_hexagram - 1}卦 · {hexagram_name}卦"
            
            if config.push_method == "console":
                print(f"\n=== {title} ===")
                print(content)
                print("=" * 30)
            elif config.push_method == "pushplus":
                push_to_pushplus(title, content)
            
            return content
            
        except Exception as e:
            return f"运行失败: {e}"

class PoetryPushTask(AutomationTask):
    """古诗推送任务"""
    
    def __init__(self):
        super().__init__(
            name="每日古诗谚语推送",
            description="每天推送一首古诗或谚语，包含原文、释义和背景故事",
            schedule=f"每天 {config.poetry_push_hour}:{config.poetry_push_minute:02d}"
        )
        self.client = MiMoClient()
        self.data_file = os.path.join(config.data_dir, "poetry_progress.json")
        self.load_progress()
    
    def load_progress(self):
        """加载进度"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.current_poem = data.get("current_poem", 1)
            else:
                self.current_poem = 1
        except Exception:
            self.current_poem = 1
    
    def save_progress(self):
        """保存进度"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump({"current_poem": self.current_poem}, f)
    
    def run(self):
        """运行古诗推送"""
        if not config.validate():
            return "配置验证失败"
        
        # 使用 MiMo API 生成内容
        prompt = f"""
请推荐一首经典的古诗或谚语（第{self.current_poem}首），包含：
1. 原文（如果是诗，注明作者和朝代）
2. 逐句释义
3. 整体白话翻译
4. 创作背景故事
5. 艺术特色分析
6. 现代启示

请选择广为流传的经典作品，用清晰、易懂的格式输出。
"""
        
        try:
            response = self.client.chat(
                messages=[{"role": "user", "content": prompt}],
                model="mimo-v2.5-pro",
                temperature=0.7,
                max_completion_tokens=2000
            )
            
            if "error" in response:
                return f"生成内容失败: {response['error']}"
            
            content = response.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            # 更新进度
            self.current_poem += 1
            self.save_progress()
            
            # 根据推送方式处理
            title = f"每日古诗谚语推送 - 第{self.current_poem - 1}首"
            
            if config.push_method == "console":
                print(f"\n=== {title} ===")
                print(content)
                print("=" * 30)
            elif config.push_method == "pushplus":
                push_to_pushplus(title, content)
            
            return content
            
        except Exception as e:
            return f"运行失败: {e}"

class CET6VocabularyTask(AutomationTask):
    """六级词汇推送任务"""
    
    def __init__(self):
        super().__init__(
            name="每日六级词汇推送",
            description="每天推送10-15个六级词汇，包含音标和释义",
            schedule="每天 7:30"
        )
        self.client = MiMoClient()
        self.data_file = os.path.join(config.data_dir, "cet6_vocab_progress.json")
        self.load_progress()
    
    def load_progress(self):
        """加载进度"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.current_day = data.get("current_day", 1)
            else:
                self.current_day = 1
        except Exception:
            self.current_day = 1
    
    def save_progress(self):
        """保存进度"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump({"current_day": self.current_day}, f)
    
    def run(self):
        """运行六级词汇推送"""
        if not config.validate():
            return "配置验证失败"
        
        prompt = f"""
请生成今天的六级词汇学习内容（第{self.current_day}天），包含10-15个六级高频词汇。

要求：
1. 每个词汇包含：
   - 单词
   - 音标（美式发音）
   - 词性
   - 中文释义
   - 例句（英文+中文翻译）
   - 记忆技巧（词根词缀或联想记忆）

2. 格式要求：
   - 使用 Markdown 格式
   - 每个词汇清晰分隔
   - 音标使用国际音标

3. 内容要求：
   - 选择六级考试高频词汇
   - 涵盖不同词性（名词、动词、形容词、副词）
   - 难度适中，适合六级备考

请生成今天的词汇内容。
"""
        
        try:
            response = self.client.chat(
                messages=[{"role": "user", "content": prompt}],
                model="mimo-v2.5-pro",
                temperature=0.7,
                max_completion_tokens=3000
            )
            
            if "error" in response:
                return f"生成内容失败: {response['error']}"
            
            content = response.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            # 更新进度
            self.current_day += 1
            self.save_progress()
            
            # 根据推送方式处理
            title = f"每日六级词汇 - 第{self.current_day - 1}天"
            
            if config.push_method == "console":
                print(f"\n=== {title} ===")
                print(content)
                print("=" * 30)
            elif config.push_method == "pushplus":
                push_to_pushplus(title, content)
            
            return content
            
        except Exception as e:
            return f"运行失败: {e}"

class AutomationManager:
    """自动化任务管理器"""
    
    def __init__(self):
        self.tasks: Dict[str, AutomationTask] = {}
        self.register_default_tasks()
    
    def register_default_tasks(self):
        """注册默认任务"""
        self.register_task(ZhouyiPushTask())
        self.register_task(PoetryPushTask())
        self.register_task(CET6VocabularyTask())
    
    def register_task(self, task: AutomationTask):
        """注册任务"""
        self.tasks[task.name] = task
    
    def run_task(self, task_name: str) -> Optional[str]:
        """运行指定任务"""
        if task_name not in self.tasks:
            print(f"任务 {task_name} 不存在")
            return None
        
        task = self.tasks[task_name]
        if not task.enabled:
            print(f"任务 {task_name} 已禁用")
            return None
        
        print(f"运行任务: {task.name}")
        return task.run()
    
    def run_all_tasks(self):
        """运行所有启用的任务"""
        results = {}
        for name, task in self.tasks.items():
            if task.enabled:
                results[name] = self.run_task(name)
        return results
    
    def list_tasks(self) -> List[Dict]:
        """列出所有任务"""
        return [
            {
                "name": task.name,
                "description": task.description,
                "schedule": task.schedule,
                "enabled": task.enabled
            }
            for task in self.tasks.values()
        ]

# 全局任务管理器
automation_manager = AutomationManager()