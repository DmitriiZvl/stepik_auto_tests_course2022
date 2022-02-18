import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("\n1 ","^_^", "\n")#выполняется 1
    yield
    print("\n5 ",":Х", "\n")#выполняется 5


@pytest.fixture()
def very_important_fixture():
    print("\n3 ",":)", "\n")#выполняется 3


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print("\n2_4 ",":-Р", "\n")#выполняется 2, 4


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
        print('FERST ')

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
        print('SECOND ')
        
        