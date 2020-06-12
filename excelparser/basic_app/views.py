from tablib import Dataset
from .resources import AddressResource
from django.shortcuts import render
from django.contrib import messages
from .models import Address

def simple_upload(request):
    if request.method == 'POST':
        address_resource = AddressResource()
        dataset = Dataset()
        new_address = request.FILES['myfile']
        print(new_address.name)
        if   new_address.name.endswith(('jpg','jpeg','png','pdf')):
            messages.error(request,'Wrong Format')
            return render(request, 'basic_app/base.html')



        imported_data = dataset.load(new_address.read())

        failed_count=0
        success_count=0
        for data in imported_data:
            # print(data)
            if (data[0]==None or data[1]==None or data[2]==None or data[3]==None or data[4]==None or data[5]==None):
                failed_count+=1

            else:
                print(data[0])
                value = Address(
                            Instruction_ID = data[0],
                            Case_Ref_No = data[1],
                            Client_Name = data[2],
                            Candidate_Name = data[3],
                            Complete_Address = data[4],
                            Period_of_Stay = data[5])

                # print(value)
                value.save()
                success_count+=1


        messages.success(request, f"Data submission successful with {success_count} records were successfully imported  and {failed_count} were failed ")
        # print(imported_data)
        # result = address_resource.import_data(dataset, dry_run=True)
        # print(result.has_errors())  # Test the data import

        # if not result.has_errors():
        #     address_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'basic_app/base.html')
