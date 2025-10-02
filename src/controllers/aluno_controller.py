from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session, joinedload
from ..config.base import SessionLocal
from ..models import Aluno

aluno_bp = Blueprint("aluno", __name__) 

@aluno_bp.route("/", methods=["GET"])
def get_alunos():
    session = SessionLocal()
    try:
        alunos = session.query(Aluno).options(joinedload(Aluno.turma)).all()
        return jsonify([{
            "id": a.id, 
            "nome": a.nome, 
            "idade": a.idade,
            "turma": a.turma.descricao,
            "data_nascimento": a.data_nascimento.isoformat() if a.data_nascimento else None,
            "nota_primeiro_semestre": a.nota_primeiro_semestre,
            "nota_segundo_semestre": a.nota_segundo_semestre,
            "media_final": a.media_final
            } for a in alunos])
    finally:
        session.close()

@aluno_bp.route("/<int:id>", methods=["GET"])
def get_aluno(id):
    session = SessionLocal()
    try:
        aluno = session.query(Aluno).options(joinedload(Aluno.turma)).get(id)
        if aluno:
            return jsonify({
                "id": aluno.id, 
                "nome": aluno.nome, 
                "idade": aluno.idade,
                "turma": aluno.turma.descricao,
                "data_nascimento": aluno.data_nascimento.isoformat() if aluno.data_nascimento else None,
                "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
                "nota_segundo_semestre": aluno.nota_segundo_semestre,
                "media_final": aluno.media_final
            })
        return jsonify({"error": "Aluno não encontrado"}), 404
    finally:
        session.close()

@aluno_bp.route("/", methods=["POST"])
def create_aluno():
    data = request.json
    session: Session = SessionLocal()
    
    try:
        aluno = Aluno(
            nome=data["nome"],
            idade=data["idade"],
            turma_id=data["turma_id"],
            data_nascimento=data.get("data_nascimento"),
            nota_primeiro_semestre=data.get("nota_primeiro_semestre"),
            nota_segundo_semestre=data.get("nota_segundo_semestre"),
            media_final=data.get("media_final")
        )
        
        session.add(aluno)
        session.commit()
        return jsonify({"message": "Aluno criado com sucesso", "id": aluno.id}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

@aluno_bp.route("/<int:id>", methods=["PUT"])
def update_aluno(id):
    data = request.json
    session: Session = SessionLocal()
    
    try:
        aluno = session.query(Aluno).get(id)
        
        if not aluno:
            return jsonify({"error": "Aluno não encontrado"}), 404
        
        aluno.nome = data.get("nome", aluno.nome)
        aluno.idade = data.get("idade", aluno.idade)
        aluno.turma_id = data.get("turma_id", aluno.turma_id)
        aluno.data_nascimento = data.get("data_nascimento", aluno.data_nascimento)
        aluno.nota_primeiro_semestre = data.get("nota_primeiro_semestre", aluno.nota_primeiro_semestre)
        aluno.nota_segundo_semestre = data.get("nota_segundo_semestre", aluno.nota_segundo_semestre)
        aluno.media_final = data.get("media_final", aluno.media_final)
        
        session.commit()
        return jsonify({"message": "Aluno atualizado com sucesso"})
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400

    finally:
        session.close()

@aluno_bp.route("/<int:id>", methods=["DELETE"])
def delete_aluno(id):
    session: Session = SessionLocal()
    
    try:
        aluno = session.query(Aluno).get(id)
        
        if not aluno:
            return jsonify({"error": "Aluno não encontrado"}), 404
        
        session.delete(aluno)
        session.commit()
        return jsonify({"message": "Aluno deletado com sucesso"})
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
