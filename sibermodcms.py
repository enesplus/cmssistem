#-- coding: UTF-8 --
# Sibermod.com cms system detect 1.0 
#Coded BY Enes Çetinkaya 

import requests
import argparse



def get(websiteToScan):
    global user_agent
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    }
    return requests.get(websiteToScan, allow_redirects=False, headers=user_agent)



def scan():
     
     
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--site", help="Taranacak alanı veya IP'yi belirtmek için bu seçeneği kullanın.")
    args = parser.parse_args()
    if args.site is None:
       
        print "    _____ _ _               __  __           _    _____               " 
        print "   / ____(_) |             |  \/  |         | |  / ____|               "
        print "  | (___  _| |__   ___ _ __| \  / | ___   __| | | |     _ __ ___  ___  "
        print "   \___ \| | '_ \ / _ \ '__| |\/| |/ _ \ / _` | | |    | '_ ` _ \/ __| " 
        print "   ____) | | |_) |  __/ |  | |  | | (_) | (_| | | |____| | | | | \__ \ "
        print "  |_____/|_|_.__/ \___|_|  |_|  |_|\___/ \__,_|  \_____|_| |_| |_|___/ "
        
        print "Domain Veya Ip Adresi Giriniz"
        print "Coded By Enes Cetinkaya -- SiberMod.com"
        websiteToScan = raw_input('Hedef Giriniz: ')
    else:
        websiteToScan = args.site

   
    if websiteToScan.startswith('http://'):
        proto = 'http://'
        
        websiteToScan = websiteToScan[7:]
    elif websiteToScan.startswith('https://'):
        proto = 'https://'
        
        websiteToScan = websiteToScan[8:]
    else:
        proto = 'http://'

    
    if websiteToScan.endswith('/'):
        websiteToScan = websiteToScan.strip('/')

    
    websiteToScan = proto + websiteToScan

    
    print
    print "Sitenin çevrimiçi olup olmadığını kontrol ediliyor ..."

    try:
        onlineCheck = get(websiteToScan)
    except requests.exceptions.ConnectionError as ex:
        print "[!] " + websiteToScan + " 404 çevrimdışı 404 "
    else:
        if onlineCheck.status_code == 200 or onlineCheck.status_code == 301 or onlineCheck.status_code == 302:
            print " |  " + websiteToScan + " çevrimiçi "
            print
            print " Tarama Basladi "
            print
            print " Sitenin yonlendirilip yonlendirilmedigin kontrol ediliyor "
            redirectCheck = requests.get(websiteToScan, headers=user_agent)
            if len(redirectCheck.history) > 0:
                if '301' in str(redirectCheck.history[0]) or '302' in str(redirectCheck.history[0]):
                    print "Girilen site yonlendiriyor gibi gorunuyor  lutfen dogru sonuclari elde etmek icin hedef siteyi dogrulayin"
                    print " 404 Sitenin yonlendirildigi anlasiliyor 404 " + redirectCheck.url
            elif 'meta http-equiv="REFRESH"' in redirectCheck.text:
                print " 404 Girilen site yönlendiriyor gibi görünüyor, lütfen doğru sonuçları elde etmek için hedef siteyi doğrulayın 404 "
            else:
                print " Site Yonlendirilmiyor "
        else:
            print "[!] " + websiteToScan + " çevrimiçi görünüyor ama bir geri döndü" + str(
                onlineCheck.status_code) + " hata ."
            print
            exit()


                    # http başlangıç 

        print
        print "HTTP başlıklarını almayı deniyorum "
    
    
        for header in onlineCheck.headers:
            try:
                print " | " + header + " : " + onlineCheck.headers[header]
            except Exception as ex:
                print "[!] Error: " + ex.message


                         #wordpress tarama başlatılıyor 
                            

        print
        print "WordPress taramaları çalıştırılıyor"

      
      
        wpLoginCheck = requests.get(websiteToScan + '/wp-login.php', headers=user_agent)
        if wpLoginCheck.status_code == 200 and "user_login" in wpLoginCheck.text and "404" not in wpLoginCheck.text:
            print "WordPress WP-Login sayfası: " + websiteToScan + '/wp-login.php'
        else:
            print " WordPress WP-Login sayfası : " + websiteToScan + '/wp-login.php'

        
        wpAdminCheck = requests.get(websiteToScan + '/wp-admin', headers=user_agent)
        if wpAdminCheck.status_code == 200 and "user_login" in wpAdminCheck.text and "404" not in wpLoginCheck.text:
            print " WordPress WP-Admin sayfası : " + websiteToScan + '/wp-admin'
        else:
            print " WordPress WP-Admin sayfası  " + websiteToScan + '/wp-admin'

        wpAdminUpgradeCheck = get(websiteToScan + '/wp-admin/upgrade.php')
        if wpAdminUpgradeCheck.status_code == 200 and "404" not in wpAdminUpgradeCheck.text:
            print " WordPress WP-Admin/upgrade.php sayfası : " + websiteToScan + '/wp-admin/upgrade.php'
        else:
            print "WordPress WP-Admin/upgrade.php sayfası : " + websiteToScan + '/wp-admin/upgrade.php'

        wpAdminReadMeCheck = get(websiteToScan + '/readme.html')
        if wpAdminReadMeCheck.status_code == 200 and "404" not in wpAdminReadMeCheck.text:
            print "WordPress Readme.html: " + websiteToScan + '/readme.html'
        else:
            print " 404  WordPress Readme.html : " + websiteToScan + '/readme.html'

        wpLinksCheck = get(websiteToScan)
        if 'wp-' in wpLinksCheck.text:
            print "WordPress wp-style bağlantıları dizininde algılandı"
        else:
            print " 404  WordPress wp tarzı bağlantılar dizinde algılanmadı  "



                        # joomla taraması başladı 




        print
        print "Joomla taraması başlatıyorum "

        joomlaAdminCheck = get(websiteToScan + '/administrator/')
        if joomlaAdminCheck.status_code == 200 and "mod-login-username" in joomlaAdminCheck.text and "404" not in joomlaAdminCheck.text:
            print " Joomla administrator giriş sayfası : " + websiteToScan + '/administrator/'
        else:
            print "  404 Joomla administrator giriş sayfası : " + websiteToScan + '/administrator/'

        joomlaReadMeCheck = get(websiteToScan + '/readme.txt')
        if joomlaReadMeCheck.status_code == 200 and "joomla" in joomlaReadMeCheck.text and "404" not in joomlaReadMeCheck.text:
            print " Joomla Readme.txt: " + websiteToScan + '/readme.txt'
        else:
            print " 404  Joomla Readme.txt  : " + websiteToScan + '/readme.txt'

        joomlaTagCheck = get(websiteToScan)
        if joomlaTagCheck.status_code == 200 and 'name="generator" content="Joomla' in joomlaTagCheck.text and "404" not in joomlaTagCheck.text:
            print " Generated by Joomla tag on index"
        else:
            print " 404 Genel by Joomla tag on index"

        joomlaStringCheck = get(websiteToScan)
        if joomlaStringCheck.status_code == 200 and "joomla" in joomlaStringCheck.text and "404" not in joomlaStringCheck.text:
            print "Joomla strings on index"
        else:
            print  " 404  Joomla strings on index  "

        joomlaDirCheck = get(websiteToScan + '/media/com_joomlaupdate/')
        if joomlaDirCheck.status_code == 403 and "404" not in joomlaDirCheck.text:
            print "Joomla media/com_joomlaupdate dizini : " + websiteToScan + '/media/com_joomlaupdate/'
        else:
            print " 404  Joomla media/com_joomlaupdate : " + websiteToScan + '/media/com_joomlaupdate/'


                    #magenta taraması başladı 



        print
        print "Magenta Taraması başlatıldı "

        magentoAdminCheck = get(websiteToScan + '/index.php/admin/')
        if magentoAdminCheck.status_code == 200 and 'login' in magentoAdminCheck.text and "404" not in magentoAdminCheck.text:
            print " Potential Magento administrator giriş sayfası : " + websiteToScan + '/index.php/admin'
        else:
            print " 404  Magento administrator giriş sayfası   : " + websiteToScan + '/index.php/admin'

        magentoRelNotesCheck = get(websiteToScan + '/RELEASE_NOTES.txt')
        if magentoRelNotesCheck.status_code == 200 and 'magento' in magentoRelNotesCheck.text:
            print " Magento Release_Notes.txt: " + websiteToScan + '/RELEASE_NOTES.txt'
        else:
            print " 404   Magento Release_Notes.txt : " + websiteToScan + '/RELEASE_NOTES.txt'

        magentoCookieCheck = get(websiteToScan + '/js/mage/cookies.js')
        if magentoCookieCheck.status_code == 200 and "404" not in magentoCookieCheck.text:
            print " Magento cookies.js : " + websiteToScan + '/js/mage/cookies.js'
        else:
            print " 404 Magento cookies.js:  + websiteToScan + '/js/mage/cookies.js'"

        magStringCheck = get(websiteToScan + '/index.php')
        if magStringCheck.status_code == 200 and '/mage/' in magStringCheck.text or 'magento' in magStringCheck.text:
            print " Magento strings on index"
        else:
            print "404 Magento strings on index"

 

        magentoStylesCSSCheck = get(websiteToScan + '/skin/frontend/default/default/css/styles.css')
        if magentoStylesCSSCheck.status_code == 200 and "404" not in magentoStylesCSSCheck.text:
            print "[Magento styles.css: " + websiteToScan + '/skin/frontend/default/default/css/styles.css'
        else:
            print " 404  Magento styles.css: " + websiteToScan + '/skin/frontend/default/default/css/styles.css'

        mag404Check = get(websiteToScan + '/errors/design.xml')
        if mag404Check.status_code == 200 and "magento" in mag404Check.text:
            print " Magento error page design.xml: " + websiteToScan + '/errors/design.xml'
        else:
            print " 404 Magento error page design.xml: " + websiteToScan + '/errors/design.xml'





                    # drupal taraması bölümü 



        print
        print "Drupal taraması başlatılıyor "

        drupalReadMeCheck = get(websiteToScan + '/readme.txt')
        if drupalReadMeCheck.status_code == 200 and 'drupal' in drupalReadMeCheck.text and '404' not in drupalReadMeCheck.text:
            print "Drupal Readme.txt: " + websiteToScan + '/readme.txt'
        else:
            print " Drupal Readme.txt : " + websiteToScan + '/readme.txt'

        drupalTagCheck = get(websiteToScan)
        if drupalTagCheck.status_code == 200 and 'name="Generator" content="Drupal' in drupalTagCheck.text:
            print "Genel by Drupal tag on index"
        else:
            print " 404 genel  by Drupal tag on index "

        drupalCopyrightCheck = get(websiteToScan + '/core/COPYRIGHT.txt')
        if drupalCopyrightCheck.status_code == 200 and 'Drupal' in drupalCopyrightCheck.text and '404' not in drupalCopyrightCheck.text:
            print " Drupal COPYRIGHT.txt: " + websiteToScan + '/core/COPYRIGHT.txt'
        else:
            print " 404 Drupal COPYRIGHT.txt  : " + websiteToScan + '/core/COPYRIGHT.txt'

        drupalReadme2Check = get(websiteToScan + '/modules/README.txt')
        if drupalReadme2Check.status_code == 200 and 'drupal' in drupalReadme2Check.text and '404' not in drupalReadme2Check.text:
            print " Drupal modules/README.txt: " + websiteToScan + '/modules/README.txt'
        else:
            print " 404  Drupal modules/README.txt  : " + websiteToScan + '/modules/README.txt'

        drupalStringCheck = get(websiteToScan)
        if drupalStringCheck.status_code == 200 and 'drupal' in drupalStringCheck.text:
            print "Drupal strings on index"
        else:
            print " 404  Drupal strings on index  "






        print
        print " phpMyAdmin Taraması başlatıldı "

        phpMyAdminCheck = get(websiteToScan)
        if phpMyAdminCheck.status_code == 200 and 'phpmyadmin' in phpMyAdminCheck.text:
            print "phpMyAdmin index sayfası "
        else:
            print " 404 phpMyAdmin dizin sayfası"

        pmaCheck = get(websiteToScan)
        if pmaCheck.status_code == 200 and 'pmahomme' in pmaCheck.text or 'pma_' in pmaCheck.text:
            print "index sayfasında phpMyAdmin pmahomme ve pma_ style bağlantıları"
        else:
            print " 404  index sayfasında phpMyAdmin pmahomme ve pma_ style bağlantıları"

        phpMyAdminConfigCheck = get(websiteToScan + '/config.inc.php')
        if phpMyAdminConfigCheck.status_code == 200 and '404' not in phpMyAdminConfigCheck.text:
            print " phpMyAdmin yapılandırma dosyası: " + websiteToScan + '/config.inc.php'
        else:
            print "  404 phpMyAdmin yapılandırma dosyası: " + websiteToScan + '/config.inc.php'

        print
        print "Tarama Bitti "
        print

scan()
