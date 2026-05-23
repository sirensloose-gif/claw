"""
配置管理模块
"""

import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

@dataclass
class Config:
    """应用配置"""
    
    # MiMo API 配置 (Token Plan)
    mimo_api_base: str = os.getenv("MIMO_API_BASE", "https://token-plan-cn.xiaomimimo.com/v1")
    mimo_api_key: str = os.getenv("MIMO_API_KEY", "")
    
    # 自动化任务配置
    automation_enabled: bool = os.getenv("AUTOMATION_ENABLED", "true").lower() == "true"
    
    # 推送时间配置（24小时制）
    zhouyi_push_hour: int = int(os.getenv("ZHOUYI_PUSH_HOUR", "8"))  # 周易推送时间
    zhouyi_push_minute: int = int(os.getenv("ZHOUYI_PUSH_MINUTE", "0"))
    
    poetry_push_hour: int = int(os.getenv("POETRY_PUSH_HOUR", "9"))  # 古诗推送时间
    poetry_push_minute: int = int(os.getenv("POETRY_PUSH_MINUTE", "0"))
    
    # 消息推送配置
    push_method: str = os.getenv("PUSH_METHOD", "console")  # console, email, webhook
    webhook_url: Optional[str] = os.getenv("WEBHOOK_URL")
    email_to: Optional[str] = os.getenv("EMAIL_TO")
    
    # 数据存储
    data_dir: str = os.getenv("DATA_DIR", "./data")
    
    def validate(self) -> bool:
        """验证配置"""
        if not self.mimo_api_key:
            print("警告: MIMO_API_KEY 未设置")
            return False
        
        if self.push_method == "webhook" and not self.webhook_url:
            print("警告: WEBHOOK_URL 未设置")
            return False
        
        if self.push_method == "email" and not self.email_to:
            print("警告: EMAIL_TO 未设置")
            return False
        
        return True

# 全局配置实例
config = Config()