# WebAPIs

In this repository, the source code of [api.towdium.me](api.towdium.me) will be given. I make it mainly for my personal use, but you are welcomed to use as well. It will be fine if you use a bandwidth less than 1G, let me know if you would like to use more.

Currently there is only unslash API. If I have time, I might add more. But it might change at any time, including functionalities and address.

## Unsplash

You might not know this site, but honestly speaking, it really cool. This site has tons of free photos for you to use. More than that, it provides online APIs for you to add random pictures to your sites. Super cool! However there is a problem, the speed sometimes goes terribly slow in mainland China.

So I made it to improve the speed. Generally speaking, it's just a proxy with a small cache. So most of time, you can get the picture super fast! Please be informed, the picture will not always change every time you refresh, especially when the network condition is bad.

### Usage

It uses http GET to provide the pictures. Currently there are 3 arguments, all optional.

- __category__: The picture category. List of categories is available at [homepage of unsplash](https://unsplash.com/). When not set, it will set to random.
- __width__: The picture width in pixel. Default is 1080.
- __height__: The picture height in pixel. Default is 720.

Long story short, it you want a nature photo with size of 1200*300, you can do like this:

```
http://api.towdium.me/unsplash?category=nature&width=800&height=300
```

Then you will get:


<img src="http://api.towdium.me/unsplash?category=nature&width=1200&height=300" alt="example" style="width:1200px;height:300px;">

