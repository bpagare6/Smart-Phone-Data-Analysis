print()

# Importing Packages
import pandas as pd
import numpy as np
import os
import glob
import ast

# Change the current directory
os.chdir("data")

# Get the name of all scraped csv file
extension = 'csv'
all_filenames = [i for i in glob.glob('page*.{}'.format(extension))]
print('All files read in ...')

# Combine all csv into one
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv("phone_data_unprocessed.csv", index=False, encoding='utf-8-sig')
print('All files combined together in phone_data_unprocessed.csv file.')

# Reading data into dataframe for preprocessing
phones = pd.read_csv('phone_data_unprocessed.csv')

# Get the Name, Ratings, Reviews, Stars
names = phones['Name'].apply(lambda x: x.split('(')[0].strip())
ratings = phones['Ratings'].apply(lambda x: x.strip().split()[0].replace(',', '')).astype(int)
reviews = phones['Reviews'].apply(lambda x: x.strip().split()[0].replace(',', '')).astype(int)
stars = phones['Stars'].astype(float)

# Actual Pre-Processing
colors, model_numbers, model_names, sim_types, hybrid_sim_slots, sim_sizes, touchscreens, rams, display_types,\
display_sizes, wifis, resolutions, batteries, otg_compatibles, audio_jacks, bluetooths, flashs, internal_storages,\
expandable_storages, weights, operating_systems, three_gs, four_gs, five_gs, cpu_cores, cpu_clock_speeds,\
no_of_primary_cameras, primary_cameras, no_of_secondary_cameras, secondary_cameras, gpss, gpus, fingerprints,\
fingerprint_types, brands = ([] for i in range(35))
for i, specification in enumerate(phones['Specifications']):
    specification = ast.literal_eval(specification)
    color, model_number, sim_type, hybrid_sim_slot, sim_size, touchscreen, ram, model_name, display_type,\
    display_size, wifi, resolution, battery, otg_compatible, audio_jack, bluetooth, flash, internal_storage,\
    expandable_storage, weight, os, three_g, four_g, five_g, cpu_core, cpu_clock_speed, no_of_primary_camera,\
    primary_camera, no_of_secondary_camera, secondary_camera, gps, gpu, fingerprint, fingerprint_type = (None for i in range(34))
    for key, value in specification.items():
        # Check if key is color
        if key.lower() == 'color':
            color = value
        # Check if key is Model Number
        elif 'model number' in key.lower():
            model_number = value
        # Check if key is Model Name
        elif 'model name' in key.lower():
            model_name = value
        # Check if key is SIM Type
        elif 'sim type' in key.lower():
            sim_type = value
        # Check if key is Hybrid Sim Slot
        elif 'hybrid sim slot' in key.lower() or 'hybrid slot' in key.lower():
            hybrid_sim_slot = value
        # Check if key is SIM Size
        elif 'sim size' in key.lower():
            sim_size = value
        # Check if key is Touchscreen
        elif 'touchscreen' in key.lower():
            touchscreen = value
        # Check if key is RAM
        elif 'RAM' in key:
            ram = value
        # Check if key is Display Type
        elif 'resolution type' in key.lower() or 'display type' in key.lower():
            display_type = value
        # Check if key is Display Size
        elif 'display size' in key.lower():
            display_size = value
        # Check if key is Resolution
        elif 'resolution' in key.lower():
            resolution = value
        # Check if key is Battery Capacity
        elif 'battery' in key.lower():
            battery = value
        # Check if key is WiFi
        elif 'wifi' in key.lower() or 'wi-fi' in key.lower():
            wifi = value
        # Check if key is OTG Compatible
        elif 'otg' in key.lower():
            otg_compatible = value
        # Check if key is Audio Jack
        elif 'audio jack' in key.lower():
            audio_jack = value
        # Check if key is Bluetooth
        elif 'bluetooth' in key.lower():
            bluetooth = value
        # Check if key is Flash
        elif 'flash' in key.lower():
            flash = value
        # Check if key is Internal Storage
        elif 'internal storage' in key.lower():
            internal_storage = value
        # Check if key is Expandable Storage
        elif 'expandable storage' in key.lower():
            expandable_storage = value
        # Check if key is Weight
        elif 'weight' in key.lower():
            weight = value
        # Check if key is Operating System
        elif 'operating system' in key.lower():
            os = value
        # Check if key is 3G, 4G, 5G
        elif '3G' in key:
            three_g = value
        elif '4G' in key:
            four_g = value
        elif '5G' in key:
            five_g = value
        elif 'network type' in key.lower():
            if '3G' in value:
                three_g = 'YES'
            if '4G' in value:
                four_g = 'YES'
            if '5G' in value:
                five_g = 'YES'
        # Check if key is Processor Core
        elif 'processor core' in key.lower():
            cpu_core = value
        # Check if key is Primary Clock Speed
        elif 'primary clock speed' in key.lower():
            cpu_clock_speed = value
        # Check if key is Primary Camera
        elif 'primary camera' == key.lower():
            camera_list = []
            for t in value.split():
                if 'MP' in t or 'yes' in t.lower():
                    camera_list.append(t)
            no_of_primary_camera = len(camera_list)
            primary_camera = ' '.join(camera_list)
        # Check if key is Secondary Camera
        elif 'secondary camera' == key.lower():
            camera_list = []
            for t in value.split():
                if 'MP' in t or 'yes' in t.lower():
                    camera_list.append(t)
            no_of_secondary_camera = len(camera_list)
            secondary_camera = ' '.join(camera_list)
        # Check if key is GPS
        elif 'gps' in key.lower():
            gps = value
        # Check if key in GPU
        elif 'gpu' in key.lower():
            gpu = value
        # Check if key is Fingerprint
        elif 'sensor' in key.lower():
            if 'fingerprint' in value.lower():
                fingerprint = 'Yes'
                if 'on-screen' in value.lower() or 'in-display' in value.lower() or 'front' in value.lower() \
                    or 'in-screen' in value.lower() or 'ultrasonic' in value.lower():
                    fingerprint_type = 'In-Display'
    # Append the data of current phone into list
    colors.append(color)
    model_numbers.append(model_number)
    model_names.append(model_name)
    sim_types.append(sim_type)
    hybrid_sim_slots.append(hybrid_sim_slot)
    sim_sizes.append(sim_size)
    touchscreens.append(touchscreen)
    rams.append(ram)
    display_types.append(display_type)
    display_sizes.append(display_size)
    wifis.append(wifi)
    resolutions.append(resolution)
    batteries.append(battery)
    otg_compatibles.append(otg_compatible)
    audio_jacks.append(audio_jack)
    bluetooths.append(bluetooth)
    flashs.append(flash)
    internal_storages.append(internal_storage)
    expandable_storages.append(expandable_storage)
    weights.append(weight)
    operating_systems.append(os)
    three_gs.append(three_g)
    four_gs.append(four_g)
    five_gs.append(five_g)
    cpu_cores.append(cpu_core)
    cpu_clock_speeds.append(cpu_clock_speed)
    no_of_primary_cameras.append(no_of_primary_camera)
    primary_cameras.append(primary_camera)
    no_of_secondary_cameras.append(no_of_secondary_camera)
    secondary_cameras.append(secondary_camera)
    gpss.append(gps)
    gpus.append(gpu)
    fingerprints.append(fingerprint)
    fingerprint_types.append(fingerprint_type)
    brands.append(names[i].split()[0])

phone_data = {'3G': three_gs, '4G': four_gs, '5G': five_gs, 'Audio Jack': audio_jacks, 'Battery': batteries,
              'Bluetooth': bluetooths, 'Brand Name': brands, 'Color': colors, 'CPU Clock Speed': cpu_clock_speeds,
              'CPU Cores': cpu_cores, 'Display Resolution': resolutions, 'Display Size': display_sizes,
              'Display Type': display_types,  'Expandable Storage': expandable_storages, 'Flash': flashs,
              'Fingerprint Scanner': fingerprints, 'Fingerprint Scanner Type': fingerprint_types, 'GPS': gpss,
              'GPU Name': gpus, 'Hybrid Slot': hybrid_sim_slots, 'Internal Storage': internal_storages,
              'Model Name': model_names, 'Model No': model_numbers, 'Name': names,
              'No of Front Cameras': no_of_secondary_cameras, 'No of Rear Cameras': no_of_primary_cameras,
              'OS': operating_systems, 'OTG Compatible': otg_compatibles, 'Primary Camera': primary_cameras,
              'RAM': rams, 'Ratings': ratings, 'Reviews': reviews, 'Stars': stars,
              'Secondary Camera': secondary_cameras, 'Sim Type': sim_types, 'Sim Size': sim_sizes,
              'Touchscreen': touchscreens, 'Weight': weights, 'WiFi': wifis}

# Convert the dictionary into DataFrame
data = pd.DataFrame(phone_data)
print('Dataframe successfully created !')

# Save the DataFrame as CSV
data.to_csv('phone_data_processed.csv', index=False)
print('Final Data stored in phone_data_processed.csv.')
print()

print('Please Note, Data is not completely preprocessed. But it is very much usable now ...')
