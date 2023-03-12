<h1 align="center" id="title">Web Kazıma için Dockerize Edilmiş Firefox</h1>

*Read this in other languages: [English](README.md), [Turkish](README.tr.md).*

<p id="description"> Web kazıma için Docker konteynerında Firefox'u çalıştırmak için örnek bir Python kodu ve Dockerfile içeren bir depo. </p>



<p id="description">Bu Selenium ve Firefox kullanarak belirtilen URL'nin sayfa kaynağını kazımak için Dockerize edilmiş bir Python betiğidir. Betik Xvfb kullanarak başsız modda çalıştırılır.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Firefox ve Selenium kullanarak belirtilen URL'nin sayfa kaynağını kazır.
*   Xvfb kullanarak başsız modda çalışır.

<h2>🛠️ Installation Steps:</h2>

<p>1. Sisteminize Docker'ı yükleyin.</p>

<p>2. Depoyu kopyalayın.</p>

<p>3. Docker görüntüsünü oluşturun.</p>

```
sudo docker build -t my-firefox .
```

<p>4. Docker konteynerını çalıştırın.</p>

```
sudo docker run --rm -e DISPLAY=:99 my-firefox
```

<p>5. Terminale URL'nin sayfa kaynağı konsola yazdırılacaktır.</p>

<h2>🍰 Contribution Guidelines:</h2>

Proje için katkılar memnuniyetle karşılanır. Bir hata bulursanız veya yeni bir özellik için bir öneriniz varsa bir sorun veya bir istek gönderisi açın.

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   Docker
*   Selenium
*   Firefox
*   Xvfb

<h2>💖Like my work?</h2>

Proje hakkında herhangi bir sorunuz varsa veya yardıma ihtiyacınız varsa lütfen GitHub üzerinde bir sorun açın.
- :beer: support me **[Patreon]**
- :coffee: support me **[buymeacoffee]** 



[buymeacoffee]: https://www.buymeacoffee.com/in/ersinaksar "buymeacoffee"
[Patreon]: https://www.buymeacoffee.com/ersinaksar "Patreon"
