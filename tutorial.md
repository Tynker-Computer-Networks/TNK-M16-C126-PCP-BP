Ethical IDOR Testing
======================
In this project, you have to find a vulnerability in a small API in a company’s website that can be used to fetch their user’s data without access or authorization. You want to report about this bug to the company and for that, you need to perform a brute force attack on the API to show them how you accessed and fetched the data without even logging in.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/c729e6cf-39b7-4b42-887c-f1ecf699121f.gif" width = "100%" height = "50%">


Follow the given steps to complete this activity.
1. Perform IDOR testing
   * Open `main.py` file.
   * Check API `http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id=1 ` for IDOR vulnerability.
   * Create a loop that goes from 1 to 5000.
   * The iterating value on the loop should be integrated in this link -
http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id=1   replacing the value of ID
   *  Print the URL if we can access data out of it.
    ```
    for i in range(1, 5000):
    URL = f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    r = requests.get(url=URL)
    if r.status_code == 200:
        print(URL)
    ```
    * Empty the cart in the session as now the order is placed.
   
   * Save and run the code to check if the product web page with prices is fixed.
