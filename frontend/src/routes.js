import Login from './components/Login.vue'
import Home from './components/Home.vue'
import LyricVocab from './components/LyricVocab.vue'
import Carousel from './components/Carousel.vue'

export const routes =[
    {
      path: '',  
      name: 'Home',
      component: Home
    },    
    {
      path: '/Login',
      name: 'Login',
      component: Login
    }, 
    {
      path: '/Lyric',
      name: 'Lyric',
      component: LyricVocab,
      props : true
    },
    {
      path: '/car',
      name: 'Carousel',
      component: Carousel
    }

  ]