<template>
  <div class="title-bar">
    <transition name="slide-down">
      <div class="title-wrapper">
        <div class="left">
          <span class="icon-back icon" @click="jumpBook"></span>
        </div>
        <div class="right">
          <div class="icon-wrapper">
            <span class="icon-mark icon" @click="showLabels"></span>
          </div>
          <div class="icon-wrapper">
            <span class="icon-note icon" @click="showNotes"></span>
          </div>
          <div class="icon-wrapper">
            <span class="icon-person icon" @click="jump"></span>
          </div>
        </div>
      </div>
    </transition>
    <transition name="slide-up">
      <div class="note-wrapper" v-show="ifSelect">
        <div class="setting-note">
          <div class="setting-color" v-for="(item, index) in highlightList" :key="index"
            @click="addHighlight(index)">
            <div class="preview" :style="{background: item}"
            :class="{'selected': index === colorNow}"></div>
          </div>
          <div class="note-operation">
            <div class="icon-wrapper">
              <span class="icon-clear icon" @click="removeHighlight"></span>
            </div>
            <div class="icon-wrapper" @click="showInput">
              <span class="icon-makeNote icon"></span>
            </div>
            <div class="icon-wrapper">
              <span class="icon-confirm icon" @click="finishiNote"></span>
            </div>
          </div>
        </div>
      </div>
    </transition>
    <transition name="slide-up">
      <textarea class="note-input" rows="20" cols="50" id="notepage"
      placeholder="请输入笔记"
      v-show="ifInputShow" ref="note">
      </textarea>
    </transition>
    <transition name="slide-left">
      <div class="note-list" v-if="ifNotesShow && !ifSelect">
        <div class="note-title"><span>笔记</span></div>
        <div class="note-item" v-for="(item, index) in noteList" :key="index">
          <div class="left" :style="{background: highlightList[item.color]}"></div>
          <div class="middle">
            <div class="up">
              <p class="content">{{"“"+item.content+"”"}}</p>
            </div>
            <div class="down">
              <textarea class="note" v-model="item.note"
              :rows="typeof(item.note)=='undefined' || item.note.length/55 < 2 ?2:item.note.length/55"
              ></textarea>
            </div>
          </div>
          <div class="right">
            <div class="icon-wrapper">
              <span class="icon-go icon" @click="jumpToNote(index)"></span>
            </div>
            <div class="icon-wrapper">
              <span class="icon-delete icon" @click="deleteNote(index)"></span>
            </div>
          </div>
        </div>
      </div>
    </transition>
    <transition name="fade">
      <div class="content-mask" 
            v-show="ifNotesShow && !ifSelect" @click="hideNotes">
      </div>
    </transition>
    <transition name="slide-left">
      <div class="label-list" v-if="ifLabelShow && !ifSelect">
        <div class="label-title">
          <div class="text-wrapper">
            <span>书签</span>
          </div>
          <div class="icon-wrapper">
            <span class="icon-add icon" @click="addLabel"></span>
          </div>
        </div>
        <div class="label-item" v-for="(item, index) in labelList" :key="index">
          <div class="left">
            <div class="icon-wrapper">
              <span class="icon-mark icon"></span>
            </div>
          </div>
          <div class="middle">
            <div class="up">
              <p class="time">{{labelList[index].time}}</p>
            </div>
            <div class="down">
              <p class="progress">{{'阅读进度：'+labelList[index].percentage+'%'}}</p>
            </div>
          </div>
          <div class="right">
            <div class="icon-wrapper">
              <span class="icon-go icon" @click="jumpToLabel(index)"></span>
            </div>
            <div class="icon-wrapper">
              <span class="icon-delete icon" @click="deleteLabel(index)"></span>
            </div>
          </div>
        </div>
      </div>
    </transition>
    <transition name="fade">
      <div class="content-mask" 
            v-show="ifLabelShow && !ifSelect" @click="hideLabels">
      </div>
    </transition>
  </div>

</template>
<script>
export default {
  props: {
    ifTitleAndMenuShow: {
      type: Boolean,
      default: false
    },
    ifSelect: {
      type: Boolean,
      default: false
    },
    highlightList: Array,
    colorNow: {
      type: Number,
      default: -1
    },
    ifInputShow: {
      type: Boolean,
      default: false
    },
    noteList: Array,
    ifNotesShow: {
      type: Boolean,
      default: false
    },
    ifLabelShow: {
      type: Boolean,
      default: false
    },
    labelList: Array,
    user_id: Number,
    book_id: Number
  },
  // data() {
  //   return {
  //     ifInputShow: false
  //   }
  // },
  methods: {
    jump() {
      let path = window.location.protocol + '//' + 'localhost:1024/self?id='+this.user_id
      window.location.href= path
    },
    jumpBook() {
      let path = window.location.protocol + '//' + 'localhost:1024/book/' + this.book_id+'?userId=' + this.user_id
      window.location.href= path
    },
    jumpToNote(index) {
      this.$emit('jumpToNote', index)
    },
    deleteNote(index) {
      this.$emit('deleteNote', index)
    },
    deleteLabel(index) {
      this.$emit('deleteLabel', index)
    },
    jumpToLabel(index) {
      this.$emit('jumpToLabel', index)
    },
    addLabel() {
      this.$emit('addLabel')
    },
    hideLabels() {
      this.$emit('hideLabels')
    },
    showLabels() {
      this.$emit('showLabels')
    },
    hideNotes() {
      this.$emit('hideNotes')
    },
    showNotes() {
      console.log(this.noteList)
      this.$emit('showNotes')
    },
    addHighlight(index) {
      this.$emit('addHighlight', index)
    },
    selectColor(index) {
      this.$emit('selectColor', index)
    },
    removeHighlight() {
      this.$emit('removeHighlight')
    },
    showInput() {
      document.getElementById('notepage').innerHTML = ''
      if (this.colorNow !== -1) {
        this.$emit('showInput')
      } else {
        alert('请先选择笔记颜色')
      }
    },
    finishiNote() {
      if (this.ifInputShow) {
        var note = this.$refs.note.value
      }
      this.$emit('finishNote', note)
    }
  }
}
</script>
<style lang="scss" scoped>
@import '../assets/styles/global';
  .title-bar {
    z-index: 102;
    .title-wrapper {
      top: 0;
      left: 0;
      z-index: 101;
      display: flex;
      width: 100%;
      height: px2rem(48);
      background: white;
      box-shadow: 0 px2rem(8) px2rem(8) rgba(0,0,0, .15);
      .left {
        flex: 0 0 px2rem(60);
        @include center;
      }
      .right {
        flex: 1;
        display: flex;
        justify-content: flex-end;
        .icon-wrapper {
          flex: 0 0 px2rem(50);
          @include center;
          .icon-note {
            font-size: px2rem(26);
          }
        }
      }
    } 
    .note-wrapper {
      position: absolute;
      bottom: 0;
      left: 0;
      z-index: 9999;
      width: 100%;
      height: px2rem(50);
      box-shadow: 0 px2rem(-8) px2rem(8) rgba(0,0,0, .15);
      .setting-note {
        height: 100%;
        display: flex;
        .setting-color {
          flex: 0 0 px2rem(60);
          display: flex;
          flex-direction: column;
          padding: px2rem(5);
          box-sizing: border-box;
          .preview {
            flex: 1;
            box-sizing: border-box;
            &.selected {
              border: px2rem(5) solid grey;
            }
          }
        }
        .note-operation {
          flex: 1;
          display: flex;
          justify-content: flex-end;
          .icon-wrapper {
            flex: 0 0 px2rem(50);
            @include center;
          }
        } 
      }
    }
    .note-input {
      position: absolute;
      bottom: px2rem(48);
      right: 0;
      z-index: 102;
      width: 30%;
      height: 30%;
      background: rgb(234, 234, 239);
      box-shadow: px2rem(-8) px2rem(-8) px2rem(8) rgba(0,0,0, .15);
    }
    .note-list {
      position: absolute;
      top: 0;
      right: 0;
      z-index: 102;
      width: 60%;
      height: 100%;
      background: white;
      overflow: auto;
      .note-title {
        height: px2rem(30);
        background: #409EFF;
        font-size: px2rem(25);
        color: white;
        padding: px2rem(10) px2rem(25);
      }
      .note-item {
        display: flex;
        min-height: px2rem(60);
        height: auto;
        overflow: auto;
        padding: px2rem(15) px2rem(15);
        border-bottom: px2rem(1) solid #f4f4f4;
        .left {
          width: 5%;
        }
        .middle {
          width: 75%;
          .up {
            min-height: px2rem(20);
            padding: px2rem(5) px2rem(10);
            font-size: px2rem(5);
            color: gray;
            line-height: px2rem(14);
            font-style: italic;
          }
          .down {
            min-height: px2rem(40);
            padding: px2rem(5) px2rem(10);
            .note {
              width: 100%;
            }
          }
        }
        .right {
          width: 20%;
          .icon-wrapper {
            flex: 0 0 px2rem(50);
            height: 50%;
            @include center;
          }
        }
      }
    }
    .label-list {
      position: absolute;
      top: 0;
      right: 0;
      z-index: 102;
      width: 30%;
      height: 100%;
      background: white;
      overflow: auto;
      .label-title {
        height: px2rem(30);
        background: #409EFF;
        font-size: px2rem(25);
        color: white;
        padding: px2rem(10) px2rem(10);
        display: flex;
        .text-wrapper {
          width: 90%;
        }
        .icon-wrapper {
          width: 10%;
          @include center;
        }
      }
      .label-item {
        display: flex;
        height: px2rem(50);
        overflow: auto;
        padding: px2rem(15) px2rem(5) px2rem(15) 0;
        border-bottom: px2rem(1) solid #f4f4f4;
        .left {
          width: 10%;
          .icon-wrapper {
            flex: 0 0 px2rem(50);
            height: 100%;
            @include center;
          }
        }
        .middle {
          width: 80%;
          .up {
            height: px2rem(20);
            padding: px2rem(5) px2rem(20);
            font-size: px2rem(5);
            color: gray;
            line-height: px2rem(14);
            font-style: italic;
          }
          .down {
            height: px2rem(25);
            padding: px2rem(5) px2rem(20);
            font-size: px2rem(10);
          }
        }
        .right {
          width: 10%;
          .icon-wrapper {
            flex: 0 0 px2rem(50);
            height: 50%;
            @include center;
          }
        }
      }
    }
    .content-mask {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 101;
      display: flex;
      width: 100%;
      height: 100%;
      background: rgba(51,51,51, .8);
    }
  }
</style>
