from typing import Dict


##TODO 다른 api 로 변경
def query(input_params: Dict[str]) -> Dict[str, str]:
    """
    Query text with params
    Args:
        input_params (Dict[str]): input dictionary
    Returns:
        Dict[str, str]: outputs
    """
    output = {
        "generated_text": "output : " + input_params["inputs"]["text"],
    }
    return output
