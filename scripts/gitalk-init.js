
const axios = require('axios');
const crypto = require('crypto');
const url = require('url');

// Helper to generate MD5 ID matching the theme's logic
function md5(text) {
  return crypto.createHash('md5').update(text).digest('hex');
}

hexo.extend.console.register('gitalk:init', 'Initialize Gitalk comments for posts', async function(args) {
  const posts = hexo.locals.get('posts');
  const config = hexo.theme.config.gitalk;
  
  if (!config || !config.clientID || !config.repo || !config.owner) {
    console.error('Gitalk config missing!');
    return;
  }

  const token = process.env.PERSONAL_TOKEN;
  if (!token) {
    console.error('PERSONAL_TOKEN is missing in environment variables!');
    return;
  }

  console.log(`Starting Gitalk initialization for ${posts.length} posts...`);
  
  // Create an Axios instance with common headers
  const api = axios.create({
    baseURL: 'https://api.github.com',
    headers: {
      'Authorization': `token ${token}`,
      'Accept': 'application/vnd.github.v3+json',
      'User-Agent': 'Hexo-Gitalk-Init'
    }
  });

  for (const post of posts.data) {
    // Logic matching themes/fluid/layout/_partials/comments/gitalk.ejs
    const id = md5(post.path);
    const title = post.title || post.slug;
    // Gitalk labels usually include 'Gitalk' and the ID
    const labels = (config.labels || ['Gitalk']).concat([id]);
    
    // Check if issue exists
    // We search issues by label matching the unique ID
    try {
      const searchRes = await api.get(`/repos/${config.owner}/${config.repo}/issues`, {
        params: {
          labels: id,
          state: 'all' // Include closed issues
        }
      });

      if (searchRes.data.length > 0) {
        console.log(`[SKIP] Issue exists for: ${title} (${id})`);
        continue;
      }

      // Create new issue
      const body = `${post.permalink}\n\n${config.body_path ? 'Visit the post to comment.' : ''}`;
      
      await api.post(`/repos/${config.owner}/${config.repo}/issues`, {
        title: title,
        body: body,
        labels: labels
      });

      console.log(`[SUCCESS] Created issue for: ${title} (${id})`);
      
      // Avoid hitting rate limits
      await new Promise(resolve => setTimeout(resolve, 1000));
      
    } catch (err) {
      console.error(`[ERROR] Failed to process ${title}:`, err.response ? err.response.data : err.message);
    }
  }
  
  console.log('Gitalk initialization complete.');
});
