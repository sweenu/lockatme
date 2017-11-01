from pathlib import Path
from lockatme.unlockers.facial_recognition import is_recognized


def test_is_recognized():
    img_dir = Path('tests/unit/unlockers/test_images')
    assert is_recognized(img_dir / 'james.jpg', img_dir / 'james2.jpg')
    assert not is_recognized(img_dir / 'james.jpg', img_dir / 'notjames.jpg')
