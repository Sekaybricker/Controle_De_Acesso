from abc import ABC, abstractmethod
from Enum import enum_tipoAluno

class Pessoa(ABC):
    
    @abstractmethod
    def __init__(self, nome: str, matricula: int, tipo_aluno: enum_tipoAluno):
        self.__nome = nome
        self.__matricula = matricula
        self.__tipo_aluno = tipo_aluno

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_tipo_pessoa(self):
        return self.__tipo_aluno

    def set_nome(self, nome):
        self.__nome = nome

    def set_matricula(self, matricula):
        self.__matricula = matricula