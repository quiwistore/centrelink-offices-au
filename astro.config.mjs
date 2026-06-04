import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://centrelinkofficesaustralia.com',
  trailingSlash: 'always',
  build: {
    format: 'directory'
  }
});
