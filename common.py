# core/registry/real_estate/schema/frame/common.py
test222222!3333333!!!!!!!!
from core.registry.common.constants import MARGIN,DELETE
def is_valid_value(v: str) -> bool:
    """余白記号もしくは抹消記号の場合はFalseを返す"""
    v = (v or "").strip()
    if not v:
        return False
    if v == MARGIN:
        return False
    if DELETE in v:
        return False
    return True