"""
自动化任务测试
"""

import unittest
import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from automation import AutomationManager, ZhouyiPushTask, PoetryPushTask

class TestAutomation(unittest.TestCase):
    """自动化任务测试"""
    
    def setUp(self):
        """测试前准备"""
        self.manager = AutomationManager()
    
    def test_list_tasks(self):
        """测试列出任务"""
        tasks = self.manager.list_tasks()
        self.assertIsInstance(tasks, list)
        self.assertGreater(len(tasks), 0)
        
        # 检查任务结构
        for task in tasks:
            self.assertIn('name', task)
            self.assertIn('description', task)
            self.assertIn('schedule', task)
            self.assertIn('enabled', task)
    
    def test_task_registration(self):
        """测试任务注册"""
        # 检查默认任务是否注册
        self.assertIn('每日周易推送', self.manager.tasks)
        self.assertIn('每日古诗谚语推送', self.manager.tasks)
        
        # 检查任务类型
        zhouyi_task = self.manager.tasks['每日周易推送']
        poetry_task = self.manager.tasks['每日古诗谚语推送']
        
        self.assertIsInstance(zhouyi_task, ZhouyiPushTask)
        self.assertIsInstance(poetry_task, PoetryPushTask)
    
    def test_task_enabled(self):
        """测试任务启用状态"""
        zhouyi_task = self.manager.tasks['每日周易推送']
        poetry_task = self.manager.tasks['每日古诗谚语推送']
        
        self.assertTrue(zhouyi_task.enabled)
        self.assertTrue(poetry_task.enabled)

if __name__ == '__main__':
    unittest.main()