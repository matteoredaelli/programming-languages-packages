def clean_text(text):
  if text is None:
    return None
  return text.replace("|", " ").replace("#", " ").replace("["," ").replace("]", " ").replace("("," ").replace(")", " ").replace("\n", " ").replace("\r", " ")


