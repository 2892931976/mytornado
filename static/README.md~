把文件解压到当前项目的目录中
命令行进入到当前目录
执行 grunt 命令可以检测是否有错误
使用grunt dev 命令进行watch，有改变时自动编译（自动调用 less:dev命令）
less: {
	    dev: {
		expand: true, cwd: './resources/less/', src: ['**/*.less'], dest: './resources/lessCss/', ext: '.css' //这里是监视目录中文件变化，并生成对应名称的css文件
		/* //注释部分是对单文件编译的配置
                options: {
                    paths: ["resources/lessCss"],
                    cleancss: false
                },
                files: {
                    "resources/lessCss/style.css": "resources/less/style.less"
                }*/
            },
}
