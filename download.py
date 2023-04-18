import gdown

# Download sample song
url = 'https://drive.google.com/uc?id=1U5B9TSl6RXTBzL6mXsMwE2sbpeMMVnZI'
output = 'model.h5'
gdown.download(url, output, quiet=False)