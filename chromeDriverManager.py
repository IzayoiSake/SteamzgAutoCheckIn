import os
import re
import wget
import zipfile
from selenium import webdriver

class ChromeDriverManager:
    def __init__(self):
        pass

    def __del__(self):
        try:
            os.remove(self.chromeDirverPath)
        except:
            pass

    def findLatestReleaseVersion(self, chrome_version):
        # url = 'https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE'
        url = 'https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_' + chrome_version
        latestRelease = wget.download(url)
        latestReleaseVersion = open(latestRelease, 'r').read().strip()
        # remove LATEST_RELEASE file
        os.remove(latestRelease)
        return latestReleaseVersion
    def donwloadChromedriver(self, chromedriver_version):
        url = 'https://storage.googleapis.com/chrome-for-testing-public/' + chromedriver_version + '/win64/chromedriver-win64.zip'
        driverZip = wget.download(url)
        # unzip the file
        with zipfile.ZipFile(driverZip, 'r') as z:
            # find the file named chromedriver.exe
            filePath = [name for name in z.namelist() if re.search(r'chromedriver.exe', name)][0]
            # extract the file 'chromedriver.exe' to the drivers/temp folder, overwrite the file if it exists
            chromeDirverPath = z.extract(filePath, path = 'drivers/temp')
        # remove the zip file
        os.remove(driverZip)
        return chromeDirverPath
    
    def checkChromeDriver(self):
        # get current chrome version in windows
        chrome_version = os.popen("reg query \"HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon\" /v version").read().split("REG_SZ")[1].strip().split(".")[0]
        # # get current chromedriver version
        # chrome_path = os.path.join("drivers", "chromedriver.exe")
        # chromedriver_version = os.popen(chrome_path + " --version").read().split("ChromeDriver ")[1].strip().split(".")[0]
        # # check if the version is matched`
        # if chrome_version != chromedriver_version:
        #     chromedriver_version = self.findLatestReleaseVersion(chrome_version)
        #     chromeDirverPath = self.donwloadChromedriver(chromedriver_version)
        # else:
        #     chromeDirverPath = chrome_path
        chromedriver_version = self.findLatestReleaseVersion(chrome_version)
        chromeDirverPath = self.donwloadChromedriver(chromedriver_version)
        self.chromeDirverPath = chromeDirverPath
        return chromeDirverPath

if __name__ == "__main__":

    def main():
        chromeManager = ChromeDriverManager()
        chromeDirverPath = chromeManager.checkChromeDriver()

    
    main()


    
        
