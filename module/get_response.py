from typing import Dict


def _request_response() -> str:
    return ""


##TODO 다른 api 로 변경
def query(input_params: Dict[str, Dict[str, str]]) -> Dict[str, str]:
    """
    Query text with params
    Args:
        input_params (Dict[str]): input dictionary
    Returns:
        Dict[str, str]: outputs
    """
    _input_text = input_params.get("inputs").get("text")
    return "output : " + _input_text


def summary_chats() -> str:
    return "summary"
