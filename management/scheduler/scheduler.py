import xml.etree.ElementTree as ET
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import threading
from management.models.add_asset import Asset

def sync_miradore():
    # Check if the previous job is still running
    if sync_miradore.is_running:
        print('Previous job still running, skipping this run')
        return

    # Set the flag to indicate that the current job is running
    sync_miradore.is_running = True

    # Run the job
    print('Running my job...')

    # Reset the flag
    sync_miradore.is_running = False

    # initialize ID to 1
    device_id = 1

    # loop through each device in Miradore
    while True:
        # make API request and parse response
        url = f'https://datasafelytest.online.miradore.com/API/' \
              f'Device/{device_id}?auth=2_ukNR8fA%7BUn68Hvu&select=InvDevice.*,' \
              f'Tag.Name,User.Email,User.LastName,User.FirstName' \
              f'&filters=InvDevice.InventoryTime%20gt%20%2724.06.2014%27&options=dateFormat=dd.MM.yyyy'
        response = requests.get(url)
        # print(response)

        # check if response status code is 404, indicating no more devices
        if response.status_code == 404:
            break

        xml_content = response.content
        # print(xml_content)

        # parse XML content
        root = ET.fromstring(xml_content)

        # find model element
        model_element = root.find('Items/Device/InvDevice/Model')
        if model_element is not None:
            model = model_element.text
        else:
            model = None
        print(f"Model: {model}")

        # find manufacturer element
        manufacturer_element = root.find('Items/Device/InvDevice/Manufacturer')
        if manufacturer_element is not None:
            manufacturer = manufacturer_element.text
        else:
            manufacturer = None
        print(f"Manufacturer: {manufacturer}")

        # find email element
        email_element = root.find('Items/Device/User/Email')
        if email_element is not None:
            email = email_element.text
        else:
            email = None
        print(f"Email: {email}")

        # find last name element
        last_name_element = root.find('Items/Device/User/Lastname')
        if last_name_element is not None:
            last_name = last_name_element.text
        else:
            last_name = None
        print(f"Last Name: {last_name}")

        # find first name element
        first_name_element = root.find('Items/Device/User/Firstname')
        if first_name_element is not None:
            first_name = first_name_element.text
        else:
            first_name = None
        print(f"First Name: {first_name}")

        # add the retrieved information to the database
        asset = Asset.objects.filter(asset_id=device_id).first()
        # update
        if asset:
            asset.asset_id=device_id,
            asset.model=model,
            asset.manufacturer=manufacturer,
            asset.first_name=first_name,
            asset.last_name=last_name,
            asset.user_email=email,
            asset.available_to_borrow=True,
            asset.save()

        # create
        else:
            Asset.objects.create(
                asset_id=device_id,
                model=model,
                manufacturer=manufacturer,
                first_name=first_name,
                last_name=last_name,
                user_email=email,
                available_to_borrow=True,
            )

        # increment ID for next iteration
        device_id += 1

    print("sync_miradore() has finished...")


def start():
    scheduler = BackgroundScheduler()
    scheduler.start()

    # Initialize the flag to indicate that no job is currently running
    sync_miradore.is_running = False

    # Schedule the job to run every 10 seconds
    scheduler.add_job(sync_miradore, 'interval', seconds=10)