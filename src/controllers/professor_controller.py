from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from ..config.base import SessionLocal
from ..models.professor import Professor

professor_bp = Blueprint("professor", __name__)

@professor_bp.route("/", methods=["GET"])
def get_professores():
    session: Session = SessionLocal()
    professores = session.query(Professor).all()
    session.close()
    return jsonify([{"id": p.id, "nome": p.nome, "materia": p.materia} for p in professores])

@professor_bp.route("/<int:id>", methods=["GET"])
def get_professor(id):
    session: Session = SessionLocal()
    professor = session.query(Professor).get(id)
    session.close()
    if professor:
        return jsonify({"id": professor.id, "nome": professor.nome, "materia": professor.materia})
    return jsonify({"error": "Professor não encontrado"}), 404

@professor_bp.route("/", methods=["POST"])
def create_professor():
    data = request.json
    
    session: Session = SessionLocal()
    
    professor = Professor(
        nome=data["nome"],
        idade=data["idade"],
        materia=data["materia"],
        observacoes=data.get("observacoes")
    )
    
    session.add(professor)
    session.commit()
    session.refresh(professor)
    session.close()

    return jsonify({"id": professor.id, "message": "Professor criado com sucesso!"}), 201
