from fastapi_sample.web.api.exception import ProjectException

ECHO_ERROR_01 = ProjectException(code="ECHO_01", msg="test", status_code=400)
