<template>
  <div>
    <h2>로또번호 추천</h2>
    <button @click="getLuckyNums">로또 번호</button>
    <!-- <h2>{{selectedLuckyNums}}</h2> -->
    <h3>로또 번호 {{ $route.params.lottoNum}}개</h3>
    <ul>
      <li v-for="(num, idx) in selectedLuckyNums" :key="idx">{{num}}</li>
    </ul>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  naem:'TheLotto',
  data: function () {
    return {
      selectedLuckyNums: [],
    }
  },
  methods: {
    getLuckyNums: function () {
      const numbers = _.range(1,46)
      this.sampleNums = _.sampleSize(numbers, this.$route.params.lottoNum)
      this.selectedLuckyNums = _.sortBy(this.sampleNums)
    }
  }
}
</script>

<style>

</style>