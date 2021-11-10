<template>
  <div id="app">
    <h1>My First Youtube Project</h1>
    <SearchBar @input-search="onInputSearch"/>
    <VideoDetail :video="selectedVideo"/>
    <VideoList :videos="videos" @select-video="onSelectVideo" />
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
// const API_KEY = 'AIzaSyDCl8U9sa3Uo70Wh6eQs1nCelpePnDcTN8'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    // SearchBar: SearchBar,의 축약문
    SearchBar,
    VideoList,
    VideoDetail
  },
  data: function () {
    return {
      inputValue: '',
      videos: [],
      selectedVideo: ''
    }
  },
  methods: {
    onInputSearch: function (inputText) {
    //onInputSearch: function (inputText, payload) {
      // console.log('데이터가 Searchbar로부터 올라옴')
      // console.log(inputText)
      // console.log(payload)
      this.inputValue = inputText
      
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue,
      }

      axios.get(API_URL, {
        params,
      })
      .then((res) => {
        console.log(res.data.items)
        this.videos = res.data.items
        console.log(this.videos)
        if (!this.selectedVideo) {
          this.selectedVideo = this.videos[0]
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    onSelectVideo: function (video) {
      this.selectedVideo =video
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
