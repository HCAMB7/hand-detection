import cv2
import imlab_feature_extraction


if __name__ == '__main__':
    img = cv2.imread("DATASET/2/", 0)				# read the input image --> You can enhance the fingerprint image using the "fingerprint_enhancer" library
    FeaturesTerminations, FeaturesBifurcations = imlab_feature_extraction.extract_minutiae_features(img, spuriousMinutiaeThresh=10, invertImage = False, showResult=True, saveResult = True)