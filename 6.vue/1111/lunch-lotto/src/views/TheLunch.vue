<template>
  <div>
    <h2>점심메뉴 추천</h2>
    <button @click="pcikOneInLunchMenu">점심 고르기</button>
    <h2>{{selectedLunchMenu}}</h2>
    <input v-model="lottoNum" placeholder="추천 받고 싶은 로또 숫자 개수 입력" type="text">
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch: ['국밥', '짜장면', '햄버거'],
      selectedLunchMenu: '',
      lottoNum: 0,
    }
  },
  methods: {
    pcikOneInLunchMenu: function () {
      const randomIndex = _.random(this.lunch.length -1)
      this.selectedLunchMenu = this.lunch[randomIndex]

      // this.$router.push('/lotto')
      this.$router.push({name:'TheLotto', params: {lottoNum: this.lottoNum}})
    },
  }
}
</script>

<style>

</style>