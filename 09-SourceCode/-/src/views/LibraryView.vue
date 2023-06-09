<template>
  <div v-if="this.isLibrary - 1 === 0" class="search-bar">
    <div style="display: flex;">
      <el-input v-model="searchInput" placeholder="搜索图书……" size="large" style="width: 300px">
        <template #prepend>
          <el-button type="primary" @click="searchBookByKey">搜索</el-button>
        </template>
      </el-input>
      <p class="search-bar-text">主类别：</p>
      <el-select v-model="firstLabel" placeholder="全部" size="large" style="width: 140px;">
        <el-option v-for="item in firstLabels" :key="item.value" :value="item.value">{{ item.value }}</el-option>
      </el-select>
      <p class="search-bar-text">副类别：</p>
      <el-select v-model="nextLabel" placeholder="全部" size="large" style="width: 140px;">
        <el-option v-for="item in getLabels(firstLabel)" :key="item" :value="item">{{ item }}</el-option>
      </el-select>
      <el-button type="primary" @click="getBookByType" size="large" style="margin: 0px 10px">搜索</el-button>
      <el-button v-if="userType == 'manager'" size="large" style="margin-left: 40px;" @click="dialogFormVisible = true">添加图书+</el-button>
      <el-button size="large" style="margin-left: 40px;" @click="back">首页</el-button>
    </div>
  </div>
  <el-divider style="margin: 0px;" />
  <div style="padding: 50px 120px;">
    <div style="display: flex; flex-wrap: wrap;">
      <LittleBook v-for="o in books" :key="o" imgName="R-C.jpg" :name="o.book_name" :rate="o.book_score" :bookId="o.book_id" :userId="this.userId" style="margin: 20px;"></LittleBook>
    </div>
  </div>

  <el-dialog title="添加图书" v-model="dialogFormVisible" width="600px">
    <el-form :model="form">
      <el-form-item label="书名：*" label-width="150px">
        <el-input v-model="form.bookName" autocomplete="off" style="width: 180px;"></el-input>
      </el-form-item>
      <el-form-item label="作者名：" label-width="150px">
        <el-input v-model="form.authorName" autocomplete="off" style="width: 180px;"></el-input>
      </el-form-item>
      <el-form-item label="主类别*" label-width="150px">
        <el-select v-model="form.label1" placeholder="请选择主类别" style="width: 180px;">
          <el-option v-for="item in firstLabels" :key="item.value" :value="item.value">{{ item.value }}</el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="副类别*" label-width="150px">
        <el-select v-model="form.label2" placeholder="请选择副类别" style="width: 180px;">
          <el-option v-for="item in getLabels(form.label1)" :key="item" :value="item">{{ item }}</el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="介绍：" label-width="150px">
        <el-input v-model="form.introduce" type="textarea" style="width: 300px;" :autosize="{minRows: 3, maxRows: 6}"></el-input>
      </el-form-item>
      <el-form-item label="URL：" label-width="150px">
        <el-input v-model="form.bookURL" autocomplete="off" style="width: 180px;"></el-input>
      </el-form-item>
    </el-form>
    <div style="display: flex; justify-content: right; padding: 0px 30px;">
      <el-button @click="dialogFormVisible = false">取 消</el-button>
      <el-button type="primary" @click="addBook()">确 定</el-button>
    </div>
  </el-dialog>
</template>

<script>
import LittleBook from '@/components/LittleBook.vue'
import { addBook, getBookId, searchBookByKey, getBookByMainType, getBookByTwoType, getBookById } from '@/api/book.js'
import { addChapters } from '@/api/chapter.js'
import { getUser } from '@/api/user.js'
import { getAuthor, addAuthor } from '@/api/author.js'
import { useRoute } from "vue-router";
import Epub from 'epubjs'
import { listStar } from '@/api/star'

export default {
  name: 'LibraryView',
  components: {
    LittleBook
  },
  data () {
    return {
      userId: "",
      userType: 'manager',
      searchInput: '',
      firstLabel: '',
      nextLabel: '',
      firstLabels: [{
        value: '哲学',
        includes: ['政治哲学', '伦理学', '认识论哲学', '逻辑学', '其他']
      },
      {
        value: '自然科学',
        includes: ['数学', '物理学', '化学', '生物学', '其他']
      },
      {
        value: '历史',
        includes: ['中国历史', '世界历史', '其他']
      },
      {
        value: '文学',
        includes: ['小说', '散文', '曲艺', '童话', '诗歌', '其他']
      },
      {
        value: '艺术',
        includes: ['艺术理论', '绘画', '音乐', '舞蹈', '其他']
      },
      {
        value: '应用科学',
        includes: ['计算机科学', '天文学', '农业科学', '其他']
      },
      {
        value: '其他',
        includes: ['其他']
      }],
      options: 0,
      books: [],
      dialogFormVisible: false,
      form: {
        bookName: '',
        label1: '',
        label2: '',
        introduce: '',
        authorName: '',
        bookURL: ''
      },
      isLibrary: 1
    }
  },
  methods: {
    back () {
      this.$router.push({ path: '/home', query: {id: this.userId} })
    },
    getLabels (theValue) {
      for (let index = 0; index < this.firstLabels.length; index++) {
        const element = this.firstLabels[index]
        if (theValue === element.value) {
          return element.includes
        }
      }
      return []
    },
    addBook () {
      if (this.form.bookName === '') {
        this.$message.error('书名不能为空')
        return
      }
      this.dialogFormVisible = false
      this.bookURL = this.form.bookURL
      addBook(this.form.bookName, this.form.label1, this.form.label2, this.form.introduce, this.form.authorName, 0, 1, this.form.bookURL).then(res => {
        console.log(res)
        getAuthor(this.form.authorName).then(res => {
          console.log(res)
          if (res.data.result === 0) {
            addAuthor(this.form.authorName, '暂无简介')
          }
        })
        this.$message.success('添加成功！')
        getBookId(this.form.bookName).then(res => {
          this.bookId = res.data.result
          this.form = { bookName: '', label1: '全部', label2: '全部', introduce: '', authorName: '', bookURL: '' }
        })
      })
      this.book = Epub(this.bookURL)
      this.book.ready.then(() => {
        console.log(this.bookId)
        this.navigation = this.book.navigation
        console.log(this.navigation)
        for (let i = 0; i < this.navigation.toc.length; i++) {
          addChapters(this.bookId, i + 1, this.navigation.toc[i].label.replace(/[ ]|[\r\n]/g, ''), this.navigation.toc[i].href)
        }
      })
    },
    searchBookByKey () {
      searchBookByKey(this.searchInput).then(res => {
        console.log(res)
        if (res.data.result === 0) {
          this.books = []
          this.$message.error('查询失败')
          return
        }
        this.books = res.data.posts
      })
    },
    getBookByType () {
      console.log(this.nextLabel === '')
      console.log(this.firstLabel !== '')
      if (this.nextLabel === '' && this.firstLabel !== '') {
        getBookByMainType(this.firstLabel).then(res => {
          console.log(res)
          if (res.data.result === 0) {
            this.books = []
            this.$message.warning('查询失败')
            this.firstLabel = ''
            this.nextLabel = ''
            return
          }
          this.books = res.data.posts
          this.firstLabel = ''
          this.nextLabel = ''
        })
      } else if (this.firstLabel !== '' && this.nextLabel !== '') {
        getBookByTwoType(this.firstLabel, this.nextLabel).then(res => {
          console.log(res)
          if (res.data.result === 0) {
            this.books = []
            this.$message.warning('查询失败')
            this.firstLabel = ''
            this.nextLabel = ''
            return
          }
          this.books = res.data.posts
          this.firstLabel = ''
          this.nextLabel = ''
        })
      } else {
        console.log('1111')
        searchBookByKey('').then(res => {
          console.log(res)
          this.books = res.data.posts
        })
      }
    }
  },
  mounted () {
    const route = useRoute();
    this.userId = route.query.id;
    this.isLibrary = route.query.isLibrary
    console.log(this.isLibrary)
    console.log(this.userId);
    getUser(this.userId).then(res => {
      console.log(res)
      if (res.data.result === 0) {
        console.log('获取信息失败')
        return
      }
      if (res.data.result.ifManager === false) this.userType = 'common'
      else this.userType = 'manager'
      console.log(this.userType)
    })
    console.log(this.isLibrary)
    console.log(this.isLibrary === 1)
    if (this.isLibrary-1 === 0) {
      searchBookByKey('').then(res => {
        console.log(res)
        this.books = res.data.posts
      })
    } else {
      listStar(this.userId).then(res => {
        console.log(res)
        const list = res.data.stars
        this.books = []
        for (let index = 0; index < list.length; index++) {
          const element = list[index];
          getBookById(element.book_id).then(r => {
            console.log(r)
            if (r.data.result - 1 === 0) {
              const b = r.data.post
              this.books.push(b)
            }
          })
        }
      })
    }
  }
}
</script>

<style scoped>
body {
  width: 1000px;
}
.search-bar {
  padding: 30px 110px;
}
.search-bar-text {
  padding: 9px 20px 9px 50px;
  margin: 0px;
  font-size: 17px;
}
.el-radio-group {
  padding: 20px 50px;
}
.dialog {
  width: 1800px;
  height: 900px
}
</style>
