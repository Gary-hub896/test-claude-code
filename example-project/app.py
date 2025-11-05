"""
简单的 Flask Web 应用示例
这个文件展示了 Claude Code 网页版如何快速创建完整的项目结构
"""

from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

# 模拟数据库
tasks = [
    {"id": 1, "title": "学习 Claude Code 网页版", "completed": True, "created_at": "2025-11-05"},
    {"id": 2, "title": "创建第一个项目", "completed": False, "created_at": "2025-11-05"},
    {"id": 3, "title": "尝试自动化 Git 操作", "completed": False, "created_at": "2025-11-05"},
]

@app.route('/')
def home():
    """主页"""
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """获取所有任务"""
    return jsonify({"tasks": tasks, "total": len(tasks)})

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """创建新任务"""
    data = request.get_json()

    new_task = {
        "id": len(tasks) + 1,
        "title": data.get('title', ''),
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }

    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """更新任务状态"""
    task = next((t for t in tasks if t['id'] == task_id), None)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    task['completed'] = data.get('completed', task['completed'])

    return jsonify(task)

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """删除任务"""
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({"message": "Task deleted"}), 200

@app.route('/health')
def health_check():
    """健康检查端点"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
