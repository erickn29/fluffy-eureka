// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  modules: [
    // '@nuxtjs/tailwindcss',
  ],
  css: [
    '/assets/css/base.css',
  ],
  plugins: [
    // 'assets/js/runHighlight.js'
  ],
  app: {
    head: {
      title: 'Python Russia',
      meta: [
        { 
          name: 'description',
          content: 'All about Python'
        }
      ],
      link: [
        { 
          rel: 'icon', 
          type: 'image/x-icon', 
          href: '/python.svg' 
        },
        {
          rel: 'stylesheet', 
          href: 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css'
        },
        {
          rel: 'stylesheet', 
          href: 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/tokyo-night-dark.css'
        },
      ],
      script: [
        {
          src: 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js'
        },
        {
          src: 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js'
        },
        {
          src: 'https://kit.fontawesome.com/bd722a61a1.js',
        }
      ]
    }
  }
})
