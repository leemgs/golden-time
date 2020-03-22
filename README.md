# Introduction

이 프로젝트는 스마트 팩토리를 위하여 딥러닝 Speech API와 IOT 센서 주변장치 (예: Motion Sensor)를 이용하여 무인 공장 자동 관리 시스템을 개발하기 위한 소스들을 구성하고 있다. 


# 설치 방법

### Raspberry Pi3 개발보드에 OS 설치
제일먼저 [doc](doc/) 폴더에 업로드 한 문서를 읽으십시오. 그리고 Raspberry Pi3 장치에 Raspbian OS를 설치하십시오.


### 무인자동화시스템 소프트웨어 설치
무인자동화시스템는 Python (모션 인식 프로그램) 및 PHP (웹 응용 프로그램) 언어를 이용하여 개발하였습니다.
다음과 같이 설치하십시오.

```bash
# windows10 PC에서 mobaxterm 소프트웨어로 ssh 세션을 실행하십시오

$ cd /var/www/html
$ sudo apt -y remove nano
$ sudo apt -y install git vim
$ sudo update-alternatives --set editor /usr/bin/vim.tiny
$ git clone https://github.com/hjoon0510/golden-time.git
$ cd ./golden-time
$ sudo chown -R www-data:www-data /var/www/html/golden-time/audio/
$ sudo visudo
--------------- /etc/sudoers: start ----------------
#includedir /etc/sudoers.d
www-data        ALL=(ALL) NOPASSWD: ALL <---- Please append a aphache webserver id here.!!!!
--------------- /etc/sudoers: ending ---------------
$ vi ./webapp/webapp_config.php  
   $db_host = 'localhost';
   $db_name = 'sbdb';
   $db_user = 'root';
   $db_pass = 'raspberry';
```

# 실행방법
웹 응용 프로그램 및 PIR Motion Sensor 프로그램을 시작하는 방법에 대해 설명합니다. 무인자동화시스템 소프트웨어는 launcher라는 프로그램을 통해서 부팅시마다 자동으로 실행됩니다. 그러므로, 아래처럼 gcc 명령으로 launcher.c를 컴파일하여주세요. 그 다음으로  컴파일하여 생성된 `launcher` 파일을 실행만 하면 됩니다.
```bash
$ cd ums
$ gcc launcher.c -o launcher 
$ ./launcher
$ firefox http://{rpi_ip_address}/ums/
```


# 참고자료
* 라즈베리파이로 시작하는 핸드메이드 IoT, https://github.com/bjpublic/raspberrypi
* 라즈베리파이 커뮤니티 사이트, https://www.raspberrypi.org/community/


