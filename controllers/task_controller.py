from flask import render_template, request, redirect, url_for
from models import db
from models.task import Task
from models.user import User

class TaskController:

    @staticmethod
    def list_tasks():
        # TODO buscar todas as tarefas do banco de dados
        tasks = Task.query.all() 
        return render_template("tasks.html", tasks=tasks)

    @staticmethod
    def create_task():
        
        if request.method == "POST":
            
            # TODO capturar dados do formulário (title, description, user_id)
            title = request.form.get("title")
            description = request.form.get("description")
            user_id = request.form.get("user_id")

            # TODO criar um novo objeto Task com os dados capturados
            new_task = Task(title=title, description=description, user_id=user_id, status="Pendente")

            # TODO adicionar no db.session e dar commit
            db.session.add(new_task)
            db.session.commit()

            return redirect(url_for("list_tasks"))

        # TODO buscar todos os usuários para exibir no <select> do formulário
        users = User.query.all()
        return render_template("create_task.html", users=users)
    
    @staticmethod
    def update_task_status(task_id):
        # TODO buscar a tarefa pelo id
        task = Task.query.get(task_id)

        # TODO: se existir, alternar status entre "Pendente" e "Concluído" e dar commit na alteração
        if task:
            task.status = "Concluído" if task.status == "Pendente" else "Pendente"
            db.session.commit()

        return redirect(url_for("list_tasks"))

    @staticmethod
    def delete_task(task_id):
        
        # TODO buscar a tarefa pelo id
        task = Task.query.get(task_id)

        # TODO: se ela existir, remover do db.session e dar commit
        if task:
            db.session.delete(task)
            db.session.commit()
    
        return redirect(url_for("list_tasks"))
