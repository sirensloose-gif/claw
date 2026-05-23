#!/usr/bin/env python3
"""
CodeBuddy/Claw - 基于 MiMo API 的 AI 聊天机器人 Agent
"""

import os
import sys
import json
import requests
from datetime import datetime
from typing import Dict, List, Optional

# 配置
MIMO_API_BASE = os.getenv("MIMO_API_BASE", "https://token-plan-cn.xiaomimimo.com/v1")
MIMO_API_KEY = os.getenv("MIMO_API_KEY", "")

class MiMoClient:
    """MiMo API 客户端"""
    
    def __init__(self, api_key: str = MIMO_API_KEY):
        self.api_key = api_key
        self.base_url = MIMO_API_BASE
        self.headers = {
            "api-key": api_key,
            "Content-Type": "application/json"
        }
    
    def chat(self, messages: List[Dict], model: str = "mimo-v2.5-pro", **kwargs) -> Dict:
        """发送聊天请求"""
        endpoint = f"{self.base_url}/chat/completions"
        payload = {
            "model": model,
            "messages": messages,
            **kwargs
        }
        
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API请求错误: {e}")
            return {"error": str(e)}

class ClawAgent:
    """Claw 聊天机器人 Agent"""
    
    def __init__(self):
        self.client = MiMoClient()
        self.conversation_history = []
    
    def chat(self, user_message: str) -> str:
        """处理用户消息并返回回复"""
        # 添加用户消息到历史
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # 调用 API
        response = self.client.chat(
            messages=self.conversation_history,
            model="mimo-v2.5-pro",
            temperature=0.7,
            max_completion_tokens=1000
        )
        
        if "error" in response:
            return f"抱歉，出现错误: {response['error']}"
        
        # 提取回复
        assistant_message = response.get("choices", [{}])[0].get("message", {}).get("content", "")
        
        # 添加助手回复到历史
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def clear_history(self):
        """清除对话历史"""
        self.conversation_history = []

def main():
    """主函数"""
    print("=== CodeBuddy/Claw 聊天机器人 ===")
    print("输入 'quit' 或 'exit' 退出")
    print("输入 'clear' 清除对话历史")
    print()
    
    agent = ClawAgent()
    
    while True:
        try:
            user_input = input("你: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit']:
                print("再见！")
                break
            
            if user_input.lower() == 'clear':
                agent.clear_history()
                print("对话历史已清除")
                continue
            
            response = agent.chat(user_input)
            print(f"Claw: {response}")
            print()
            
        except KeyboardInterrupt:
            print("\n再见！")
            break
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()