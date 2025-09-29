from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session, joinedload
from ..config.base import SessionLocal
from ..models.professor import Professor

professor_bp = Blueprint("professor", __name__)

@professor_bp.route("/", methods=["GET"])
def get_professores():
    session: Session = SessionLocal()
    try:
        professores = session.query(Professor).options(joinedload(Professor.turmas)).all()
        return jsonify([{
            "id": p.id, 
            "nome": p.nome, 
            "materia": p.materia,
            "turmas": [{
                "id": t.id,
                "descricao": t.descricao
            } for t in p.turmas]
        } for p in professores])
    finally:
        session.close()

@professor_bp.route("/<int:id>", methods=["GET"])
def get_professor(id):
    session: Session = SessionLocal()
    try:
        professor = session.query(Professor).options(joinedload(Professor.turmas)).get(id)
        
        if professor:
            return jsonify({
                "id": professor.id, 
                "nome": professor.nome, 
                "materia": professor.materia,
                "turmas": [{
                    "id": t.id,
                    "descricao": t.descricao
                } for t in professor.turmas]
            })
        
        return jsonify({"error": "Professor não encontrado"}), 404
    finally:
        session.close()

@professor_bp.route("/", methods=["POST"])
def create_professor():
    data = request.json
    session: Session = SessionLocal()
    
    try:
        professor = Professor(
            nome=data["nome"],
            idade=data["idade"],
            materia=data["materia"],
            observacoes=data.get("observacoes")
        )
        
        session.add(professor)
        session.commit()
        session.refresh(professor)
        return jsonify({"id": professor.id, "message": "Professor criado com sucesso!"}), 201
    finally:
        session.close()

@professor_bp.route("/<int:id>", methods=["PUT"])
def update_professor(id):
    data = request.json
    session: Session = SessionLocal()
    
    try:
        professor = session.query(Professor).get(id)
        
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404
        
        professor.nome = data.get("nome", professor.nome)
        professor.idade = data.get("idade", professor.idade)
        professor.materia = data.get("materia", professor.materia)
        professor.observacoes = data.get("observacoes", professor.observacoes)
        
        session.commit()
        session.refresh(professor)
        return jsonify({"id": professor.id, "message": "Professor atualizado com sucesso!"})
    finally:
        session.close()

@professor_bp.route("/<int:id>", methods=["DELETE"])
def delete_professor(id):
    session: Session = SessionLocal()
    
    try:
        professor = session.query(Professor).get(id)
        
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404
        
        session.delete(professor)
        session.commit()
        return jsonify({"message": "Professor deletado com sucesso!"})
    finally:
        session.close()