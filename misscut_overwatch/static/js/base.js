const PAST_MISTAKE_TYPE_MAP = {
    1: "别字词错误",
    2: "缺字错误",
    3: "重复字词错误",
    4: "乱序错误",
    5: "乱序错误",
    6: "重复字词错误"
};

const NEW_MISTAKE_TYPE_MAP = {
    '1': "建议替换",
    '2': "建议替换",
    '3': "遗漏字词，建议补充",
    '4': "冗余字词，建议删去",
    '5': "建议替换",
    '6': "建议替换",
    '7': "建议调整语序"
};
let more_mistakes_flag = false;

const MISTAKE_TYPE_MAP = NEW_MISTAKE_TYPE_MAP;

function to_html(text) {
    return text.replace(/</g, '&lt;').replace(/>/g, '&gt;')
}
