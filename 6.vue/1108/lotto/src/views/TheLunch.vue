<template>
  <div>

    <h1>점심메뉴</h1>
    <button @click="pickOne">Pick Lunch</button>
    <p>{{ choice }}</p>

  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch: ['국밥', '짜장면', '햄버거'],
      choice: '',
    }
  },
  methods: {
    pickOne: function () {
      this.choice = _.sample(this.lunch)
    }
  }
}
</script>