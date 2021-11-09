<template>
  <div>
    <!-- 하나의 컴포넌트에는 하나의 태그만 있어야 한다 -->
    <h1>This is parent</h1>
    <p>ParentData: {{ parentData }}</p>
    <input v-model="parentData" type="text" @input="inputParentData">
    <p>appData: {{ appData }}</p>
    <p>ChildData: {{ childData }}</p>
    <Child :appData="appData" :parentData="parentData" 
    @child-input="inputChildData" />
  </div>
</template>

<script>
import Child from './Child.vue'
export default {
  // vue로 볼때 이름 표시를 해주는 기능
  name: 'Parent',
  data: function () {
    return {
      parentData: '',
      childData: '',
    }
  },
  methods: {
    inputChildData: function (data) {
      this.childData = data
      this.$emit('child-input', this.childData)
      // console.log('!! text from child')
    },
    inputParentData: function () {
      this.$emit('parent-input', this.parentData)
    }
  },
  // 부모에게서 받을 내용은 props
  props: {
    appData: String
  },
  components: {
    Child,
  }
}
</script>

<style>

</style>