from main import StudentsInMLOps

def test_enrollStudents():
    s = StudentsInMLOps()
    s.enrollStudents(5)
    assert s.getTotalStrength() == 5

def test_dropStudents():
    s = StudentsInMLOps()
    s.enrollStudents(10)
    s.dropStudents(3)
    assert s.getTotalStrength() == 7

def test_getClassName():
    s = StudentsInMLOps()
    assert s.getClassName() == "StudentsInMLOps"
