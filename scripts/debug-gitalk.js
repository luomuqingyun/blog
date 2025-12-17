
const crypto = require('crypto');

function md5(text) {
    return crypto.createHash('md5').update(text).digest('hex');
}

hexo.extend.console.register('debug:gitalk', 'Debug Gitalk ID generation', async function (args) {
    await this.load(); // Force load source files
    const posts = hexo.locals.get('posts');

    console.log('Total posts:', posts.length);

    posts.forEach(post => {
        const id = md5(post.path);
        console.log(`Title: ${post.title}`);
        console.log(`Path:  ${post.path}`);
        console.log(`MD5:   ${id}`);
        console.log('---');
    });
});
