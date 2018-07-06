const uploadFileUrl = 'https://ai.kilig.com.cn/test/'


Page({
  data: {
    imageSrc: null,
  },
  chooseImage: function () {
    var that = this
    wx.chooseImage({
      sourceType: ['camera', 'album'],
      sizeType: ['compressed'],
      count: 1,
      success: function (res) {
        console.log(res)
        that.setData({
          imageSrc: res.tempFilePaths[0]
        })
      }
    })
  },
  check: function (e) {
    var that = this
    wx.uploadFile({
      url: uploadFileUrl,
      name: 'picture',
      filePath: that.data.imageSrc,
      formData: {
        'user': 'test'
      },
      success: function (res) {
        console.log('imageSrc is:', that.data.imageSrc)
        console.log('uploadImage success, res is:', res)
        wx.showModal({
          title: "图片详情",
          content: res.data,
          showCancel: false,
          confirmText: "确定"
        })
      },
      fail: function ({errMsg}) {
        console.log('uploadImage fail, errMsg is', errMsg)
      }
    })
  },
  reload: function (e) {
    this.setData({
      imageSrc: null
    })
  }
})

