# WebAPIs

In this repository, the source code of [api.towdium.me](api.towdium.me)
will be given. I make it mainly for my personal use, but you are 
welcomed to use as well. It will be fine if you use a bandwidth 
less than 1G, let me know if you would like to use more.

Currently there is only unslash API. If I have time, I might add more.
But it might change at any time, including functionalities and address.

## Unsplash

You might not know this site, but honestly speaking, it really cool.
This site has tons of free photos for you to use. More than that,
it provides online APIs for you to add random pictures to your sites.
Super cool! However there is a problem, the speed sometimes goes
terribly slow in mainland China.

So I made it to improve the speed. Generally speaking, it's just a
proxy with a small cache. So most of time, you can get the picture
super fast! The unsplash api seems to provide the same picture in
one second, while I'm trying to make it different for each refresh.

### Usage

__The old usage has been deprecated since 20th Oct 2017!__

You can use it nearly identical to original unsplash syntax.
Here is an example.

If you unsplash link is:

```
https://source.unsplash.com/category/nature/
```

All you need is use the following address instead:

```
http://api.towdium.me/unsplash/category/nature/
```

Sorry for no https support. But don't worry since it's just pictures.
For the syntax documentation, please go to [unsplash's documentation][2]
If you want to have a try, here is the link: [example picture][2]


## Unblock

__This will have no use in China mainland!__

Since I'm having a little server in mainland China, there is
a proxy serve set up for users to get back to China mainland.
Again, it cannot unblock sites like youtube or twitter, please
be informed.

To use it, first you need a device that supports PAC proxy,
or something usually called automatically configured proxy.
Then all you need to do is set the PAC address to
[http://api.towdium.me/unblock/pac.pac][3].

The work is done basing on Unblock Youku's works. Although
the source is open, you can refer to it, but you are allowed
to use the source somewhere else. Generally speaking,
All Rights Reserved for the code in unblock module.

[1]: https://source.unsplash.com/
[2]: http://api.towdium.me/unsplash/unsplash/collection/327760
[3]: http://api.towdium.me/unblock/pac.pac