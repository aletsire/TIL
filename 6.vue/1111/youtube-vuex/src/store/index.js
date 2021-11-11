import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    searchResult: [],
    selectdVideo:null,
  },
  mutations: {
    ADD_SEARCH_RESULT: function (state, items) {
      state.searchResult = items
    },
    SELECT_VIDEO: function (state,video) {
      state.selectdVideo = video
    }
  },
  actions: {
    // commit = context.commit
    onSearch: function ({commit}, query) {
    // onSearch: function (context, query) {
      axios.get(API_URL, {
        params: {
          part: 'snippet',
          q: query,
          key: API_KEY,
          type: 'video',
        }
      })
      .then(res => {
        commit('ADD_SEARCH_RESULT', res.data.items)
        // context.commit('ADD_SEARCH_RESULT', res.data.items)
      })
      .catch(err => {
        console.log(err)
      })
    },

    selectVideo: function ({commit}, video) {
    // selectVideo: function (context, video) {
      commit('SELECT_VIDEO',video)
      // context.commit('SELECT_VIDEO',video)
    }
  },
  getters: {
    //선택된 비디오가 있는지 확인
    isSelected: function (state) {
      return state.selectdVideo !== null
    },
    // Video Url만들기
    videoUrl: function (state) {
      if (state.selectdVideo) {
        const videoId = state.selectdVideo.id.videoId
        return `https://www.youtube.com/embed/${videoId}`
      }
      return ''
    },
    //선택된 비디오 제목 리턴
    videoTitle: function (state) {
      if (state.selectdVideo) {
        const title = state.selectdVideo.snippet.title
        return _.unescape(title)
      }
      return ''
    },
    videoDesc: function(state) {
      if (state.selectdVideo) {
        const desc = state.selectdVideo.snippet.description
        return _.unescape(desc)
      }
      return ''
    }
  },
  modules: {
  }
})
