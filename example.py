import numpy as np
from sklearn.manifold import TSNE
from matplotlib.pyplot import scatter, show

# Load the final layer activations
activations = # Load your activations data here (e.g., from a saved file)

# Extract features and labels (if available)
features = activations # If activations already contain features, use directly
labels = None # Optional: If you have labels for your data, store them here

# Apply dimensionality reduction with t-SNE
tsne = TSNE(n_components=2)
reduced_activations = tsne.fit_transform(features)

# Create a function to generate slide images for each data point
def generate_slide_image(activation):
  # Implement your logic here to generate an image based on the activation values
  # This could involve reshaping, scaling, or applying specific transformations
  # Example: reshape activation to a desired image size and normalize values
  image = activation.reshape(image_height, image_width)
  image = (image - activation.min()) / (activation.max() - activation.min())
  return image

# Generate slide images for all data points
slide_images = [generate_slide_image(activation) for activation in activations]

# Scatter plot the reduced activations with corresponding slide images
scatter(reduced_activations[:, 0], reduced_activations[:, 1], c=labels)
for i, point in enumerate(reduced_activations):
  show(slide_images[i])
  # Use appropriate methods to display each slide image next to its corresponding point

show()
