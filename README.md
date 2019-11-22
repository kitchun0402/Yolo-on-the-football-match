# Result: https://drive.google.com/file/d/1yWS9RBq2bUwYFp3MytlyzZ9p5ZEmLwzP/view?usp=sharing

# Labels: Player, Football, Goalpost, Referee, Holding the ball

# Steps:
1. Download images from the target video (only select images with wide shot by using existing yolo model to do filtering)
2. Draw bounding boxes (annotaion) and output xml files
3. Train the model by using yolov2_voc and grayscale images on Google Colab
4. Output a video
  - Load a video
  - Turn each color frame into the grayscale frame and make the prediction
  - Put the bounding box back to the color frame
  - Find the color range to seperate two teams
  - Calculate distances to draw two arrows for each football player, which show the two shorten distance to the player's teammate

# Limitation:
Only around 230 images are selected from the video (around 1.5 hours) which leads to insufficient data for some of the rare labels e.g. Football, Goalpost
