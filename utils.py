def clean_text(text):
  return text.replace("|", " ").replace("#", " ").replace("["," ").replace("]", " ").replace("("," ").replace(")", " ").replace("\n", " ").replace("\r", " ")


