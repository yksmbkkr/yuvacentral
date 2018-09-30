var CACHE = 'YUVA';

self.addEventListener('install', function (event) {
    event.waitUntil(
        caches.open(CACHE).then(function (cache) {
            return cache.addAll([
                '/',
                '/login'
            ]);
        })
    );
});

self.addEventListener('fetch', function(evt) {
    console.log('The service worker is serving the asset.');
    evt.respondWith(fromCache(evt.request));
    evt.waitUntil(
        update(evt.request)
        .then(refresh)
    );
});

function fromCache(request) {
    return caches.open(CACHE).then(function (cache) {
        return cache.match(request);
    });
}

function update(request) {
    return caches.open(CACHE).then(function (cache) {
      return fetch(request).then(function (response) {
        return cache.put(request, response.clone()).then(function () {
          return response;
        });
      });
    });
  }

  function refresh(response) {
    return self.clients.matchAll().then(function (clients) {
      clients.forEach(function (client) {
        var message = {
            type: 'refresh',
            url: response.url,
            eTag: response.headers.get('ETag')
        };
        client.postMessage(JSON.stringify(message));
    });
  });
}


// self.addEventListener('fetch', function (event) {
//     var requestUrl = new URL(event.request.url);
//     if (requestUrl.origin === location.origin) {
//         if ((requestUrl.pathname === '/')) {
//             event.respondWith(caches.match('/'));
//             return;
//         }
//     }
//     event.respondWith(
//         //fetch(event.request).catch(function() {
//             //return caches.match(event.request);
//         caches.match(event.request).then(function (response) {
//             return response || fetch(event.request);
//         })
//     );
// });

// self.addEventListener('activate', (event) => {
//     // Clean up old cache versions
// });