from unsupervised_llamas.label_scripts import segmentation_labels as sl
from PIL import Image
import numpy as np
import glob 


if __name__ == '__main__':
	"""
	Završni rad: Semantička segmentacija kolničkih trakova
	--------------------------------------------------------------------------------------------
	Autorica: Jelena Bratulić, 0036506909
	"""
	
	path_save_train = 'C:\\zavrsni\\paper_rez\\train_slike\\'
	path_train1 = 'C:\\zavrsni\\llamas\\grayscale_images\\train\\images-2014-12-18-14-17-05\\'
	path_train2 = 'C:\\zavrsni\\llamas\\grayscale_images\\train\\images-2014-12-18-14-28-45\\'
	path_train3 = 'C:\\zavrsni\\llamas\\grayscale_images\\train\\images-2014-12-18-14-43-48\\'
	path_train4 = 'C:\\zavrsni\\llamas\\grayscale_images\\train\\images-2014-12-22-12-02-45_mapping_280N_ramps\\'
	path_train5 = 'C:\\zavrsni\\llamas\\grayscale_images\\train\\images-2014-12-22-13-04-51_mapping_280N_2nd_lane\\'
	path_train6 = 'C:\\zavrsni\\llamas\\grayscale_images\\train\\images-2014-12-22-14-01-36_mapping_280N_3rd_lane\\'
	path_train7 = 'C:\\zavrsni\\llamas\\grayscale_images\\train\\images-2014-12-22-14-36-42_mapping_280N_4th_lane\\'
	path_train8 = 'C:\\zavrsni\\llamas\\grayscale_images\\train\\images-2014-12-22-15-18-11_mapping_RTC_to_280_left_lanes\\'

	photo_from_dir1 = list(glob.glob(path_train1+'*.png'))
	photo_from_dir2 = list(glob.glob(path_train2 + '*.png'))
	photo_from_dir3 = list(glob.glob(path_train3 + '*.png'))
	photo_from_dir4 = list(glob.glob(path_train4 + '*.png'))
	photo_from_dir5 = list(glob.glob(path_train5 + '*.png'))
	photo_from_dir6 = list(glob.glob(path_train6 + '*.png'))
	photo_from_dir7 = list(glob.glob(path_train7 + '*.png'))
	photo_from_dir8 = list(glob.glob(path_train8 + '*.png'))

	photo_dirs = [photo_from_dir1, photo_from_dir2, photo_from_dir3, photo_from_dir4,
				  photo_from_dir5, photo_from_dir6, photo_from_dir7, photo_from_dir8]
	
	for photo_dir in photo_dirs:
		i = 0
		for photo in photo_dir:
			if i == 300:
				break
			full_path = photo.split('\\')
			name = full_path[-1]
			photo_normal = Image.open(photo)
			photo_small = photo_normal.crop((0,333, 1276, 717))
			photo_small = photo_normal.resize((960, 288))
			photo_small.save(path_save_train+name)
			i += 1
			

	path_save_test = 'C:\\zavrsni\\paper_rez\\test_slike\\'
	path_test = 'C:\\zavrsni\\llamas\\grayscale_images\\valid\\images-2014-12-22-14-19-07_mapping_280S_3rd_lane\\'
	photo_from_test = list(glob.glob(path_test + '*.png'))

	for photo in photo_from_test:
			full_path = photo.split('\\')
			name = full_path[-1]
			photo_normal = Image.open(photo)
			photo_small = photo_normal.crop((0, 333, 1276, 717))
			photo_small = photo_normal.resize((960, 288))
			photo_small.save(path_save_test+name)
			
	path_save_valid = 'C:\\zavrsni\\paper_rez\\valid_slike\\'
	path_valid = 'C:\\zavrsni\\llamas\\grayscale_images\\valid\\images-2014-12-22-12-35-10_mapping_280S_ramps\\'
	photo_from_valid = list(glob.glob(path_valid + '*.png'))

	for photo in photo_from_valid:
			full_path = photo.split('\\')
			name = full_path[-1]
			photo_normal = Image.open(photo)
			photo_small = photo_normal.crop((0, 333, 1276, 717))
			photo_small = photo_normal.resize((960, 288))
			photo_small.save(path_save_valid+name)
			

	path_save_train_labels = 'C:\\zavrsni\\paper_rez\\train_labele_multi\\'
	path_save_all_train_labels = 'C:\\zavrsni\\llamas\\labels\\train\\train_all_labels_small_ids_multi\\'
	path_train_l1 = 'C:\\zavrsni\\llamas\\labels\\train\\images-2014-12-18-14-17-05\\'
	path_train_l2 = 'C:\\zavrsni\\llamas\\labels\\train\\images-2014-12-18-14-28-45\\'
	path_train_l3 = 'C:\\zavrsni\\llamas\\labels\\train\\images-2014-12-18-14-43-48\\'
	path_train_l4 = 'C:\\zavrsni\\llamas\\labels\\train\\images-2014-12-22-12-02-45_mapping_280N_ramps\\'
	path_train_l5 = 'C:\\zavrsni\\llamas\\labels\\train\\images-2014-12-22-13-04-51_mapping_280N_2nd_lane\\'
	path_train_l6 = 'C:\\zavrsni\\llamas\\labels\\train\\images-2014-12-22-14-01-36_mapping_280N_3rd_lane\\'
	path_train_l7 = 'C:\\zavrsni\\llamas\\labels\\train\\images-2014-12-22-14-36-42_mapping_280N_4th_lane\\'
	path_train_l8 = 'C:\\zavrsni\\llamas\\labels\\train\\images-2014-12-22-15-18-11_mapping_RTC_to_280_left_lanes\\'

	label_from_dir1 = list(glob.glob(path_train_l1 + '*.json'))
	label_from_dir2 = list(glob.glob(path_train_l2 + '*.json'))
	label_from_dir3 = list(glob.glob(path_train_l3 + '*.json'))
	label_from_dir4 = list(glob.glob(path_train_l4 + '*.json'))
	label_from_dir5 = list(glob.glob(path_train_l5 + '*.json'))
	label_from_dir6 = list(glob.glob(path_train_l6 + '*.json'))
	label_from_dir7 = list(glob.glob(path_train_l7 + '*.json'))
	label_from_dir8 = list(glob.glob(path_train_l8 + '*.json'))

	label_dirs = [label_from_dir1, label_from_dir2, label_from_dir3, label_from_dir4,
				  label_from_dir5, label_from_dir6, label_from_dir7, label_from_dir8]

	for label_dir in label_dirs:
		i = 0
		for label in label_dir:	
			if i == 300:
				break
			prazna = np.zeros((717,1276))
			data = label.strip('\n').split('\\')
			ime = data[-1].split('.')
			save_name1 = path_save_train_labels+ime[0]+'.png'
			save_name2 = path_save_all_train_labels+ime[0]+'.png'
			slika = sl.create_multi_class_segmentation_label(label.strip('\n'))
			
			indeks0 = np.where(slika[:,:,0] == 1)
			indeks1 = np.where(slika[:,:,1] == 1)
			indeks2 = np.where(slika[:,:,2] == 1)
			indeks3 = np.where(slika[:,:,3] == 1)
			indeks4 = np.where(slika[:,:,4] == 1)
			
			prazna[indeks0] = 0
			prazna[indeks1] = 1
			prazna[indeks2] = 2
			prazna[indeks3] = 3
			prazna[indeks4] = 4
			prazna = prazna.astype(np.uint8)
			
			
			prikaz = Image.fromarray(prazna)
			prikaz = prikaz.crop((0, 333, 1276, 717))
			prikaz = prikaz.resize((960,288), resample=Image.NEAREST)
			prikaz.save(save_name2)
			prikaz.save(save_name1)
			i += 1
		

	

	path_save_test_labels = 'C:\\zavrsni\\paper_rez\\test_labele_multi\\'
	path_test_l = 'C:\\zavrsni\\llamas\\labels\\valid\\images-2014-12-22-14-19-07_mapping_280S_3rd_lane\\'
	photo_from_test_l = list(glob.glob(path_test_l + '*.json'))
	
	for path in photo_from_test_l:
		data = path.strip('\n').split('\\')
		ime = data[-1].split('.')
		save_name = path_save_test_labels+ime[0]+'.png'
		prazna = np.zeros((717,1276))
		
		slika = sl.create_multi_class_segmentation_label(path.strip('\n'))
		
		indeks0 = np.where(slika[:,:,0] == 1)
		indeks1 = np.where(slika[:,:,1] == 1)
		indeks2 = np.where(slika[:,:,2] == 1)
		indeks3 = np.where(slika[:,:,3] == 1)
		indeks4 = np.where(slika[:,:,4] == 1)
		
		prazna[indeks0] = 0
		prazna[indeks1] = 1
		prazna[indeks2] = 2
		prazna[indeks3] = 3
		prazna[indeks4] = 4
		
		prazna = prazna.astype(np.uint8)
		prikaz = Image.fromarray(prazna)
		prikaz = prikaz.crop((0, 333, 1276, 717))
		prikaz = prikaz.resize((960,288), resample=Image.NEAREST)
		prikaz.save(save_name)
		
	path_save_valid_labels = 'C:\\zavrsni\\paper_rez\\valid_labele_multi\\'
	path_valid_l = 'C:\\zavrsni\\llamas\\labels\\valid\\images-2014-12-22-14-19-07_mapping_280S_ramps\\'
	photo_from_valid_l = list(glob.glob(path_valid_l + '*.json'))
	
	for path in photo_from_valid_l:
		data = path.strip('\n').split('\\')
		ime = data[-1].split('.')
		save_name = path_save_valid_labels+ime[0]+'.png'
		prazna = np.zeros((717,1276))
		
		slika = sl.create_multi_class_segmentation_label(path.strip('\n'))
		
		indeks0 = np.where(slika[:,:,0] == 1)
		indeks1 = np.where(slika[:,:,1] == 1)
		indeks2 = np.where(slika[:,:,2] == 1)
		indeks3 = np.where(slika[:,:,3] == 1)
		indeks4 = np.where(slika[:,:,4] == 1)
		
		prazna[indeks0] = 0
		prazna[indeks1] = 1
		prazna[indeks2] = 2
		prazna[indeks3] = 3
		prazna[indeks4] = 4
		
		prazna = prazna.astype(np.uint8)
		prikaz = Image.fromarray(prazna)
		prikaz = prikaz.crop((0, 333, 1276, 717))
		prikaz = prikaz.resize((960,288), resample=Image.NEAREST)
		prikaz.save(save_name)
