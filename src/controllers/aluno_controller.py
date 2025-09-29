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