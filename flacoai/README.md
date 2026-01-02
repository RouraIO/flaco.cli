<p align="center">
    <a href="https://flacoai.chat/"><img src="https://flacoai.chat/assets/logo.svg" alt="flacoai Logo" width="300"></a>
</p>

<h1 align="center">
AI Pair Programming in Your Terminal
</h1>


<p align="center">
flacoai lets you pair program with LLMs to start a new project or build on your existing codebase. 
</p>

<p align="center">
  <img
    src="https://flacoai.chat/assets/screencast.svg"
    alt="flacoai screencast"
  >
</p>

<p align="center">
<!--[[[cog
from scripts.homepage import get_badges_md
text = get_badges_md()
cog.out(text)
]]]-->
  <a href="https://github.com/RouraIO/flaco.cli/stargazers"><img alt="GitHub Stars" title="Total number of GitHub stars the flacoai project has received"
src="https://img.shields.io/github/stars/RouraIO/flaco.cli?style=flat-square&logo=github&color=f1c40f&labelColor=555555"/></a>
  <a href="https://pypi.org/project/flacoai-chat/"><img alt="PyPI Downloads" title="Total number of installations via pip from PyPI"
src="https://img.shields.io/badge/📦%20Installs-4.1M-2ecc71?style=flat-square&labelColor=555555"/></a>
  <img alt="Tokens per week" title="Number of tokens processed weekly by flacoai users"
src="https://img.shields.io/badge/📈%20Tokens%2Fweek-15B-3498db?style=flat-square&labelColor=555555"/>
  <a href="https://openrouter.ai/#options-menu"><img alt="OpenRouter Ranking" title="flacoai's ranking among applications on the OpenRouter platform"
src="https://img.shields.io/badge/🏆%20OpenRouter-Top%2020-9b59b6?style=flat-square&labelColor=555555"/></a>
  <a href="https://flacoai.chat/HISTORY.html"><img alt="Singularity" title="Percentage of the new code in flacoai's last release written by flacoai itself"
src="https://img.shields.io/badge/🔄%20Singularity-88%25-e74c3c?style=flat-square&labelColor=555555"/></a>
<!--[[[end]]]-->  
</p>

## Features

### [Cloud and local LLMs](https://flacoai.chat/docs/llms.html)

<a href="https://flacoai.chat/docs/llms.html"><img src="https://flacoai.chat/assets/icons/brain.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
flacoai works best with Claude 3.7 Sonnet, DeepSeek R1 & Chat V3, OpenAI o1, o3-mini & GPT-4o, but can connect to almost any LLM, including local models.

<br>

### [Maps your codebase](https://flacoai.chat/docs/repomap.html)

<a href="https://flacoai.chat/docs/repomap.html"><img src="https://flacoai.chat/assets/icons/map-outline.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
flacoai makes a map of your entire codebase, which helps it work well in larger projects.

<br>

### [100+ code languages](https://flacoai.chat/docs/languages.html)

<a href="https://flacoai.chat/docs/languages.html"><img src="https://flacoai.chat/assets/icons/code-tags.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
flacoai works with most popular programming languages: python, javascript, rust, ruby, go, cpp, php, html, css, and dozens more.

<br>

### [Git integration](https://flacoai.chat/docs/git.html)

<a href="https://flacoai.chat/docs/git.html"><img src="https://flacoai.chat/assets/icons/source-branch.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
flacoai automatically commits changes with sensible commit messages. Use familiar git tools to easily diff, manage and undo AI changes.

<br>

### [Use in your IDE](https://flacoai.chat/docs/usage/watch.html)

<a href="https://flacoai.chat/docs/usage/watch.html"><img src="https://flacoai.chat/assets/icons/monitor.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Use flacoai from within your favorite IDE or editor. Ask for changes by adding comments to your code and flacoai will get to work.

<br>

### [Images & web pages](https://flacoai.chat/docs/usage/images-urls.html)

<a href="https://flacoai.chat/docs/usage/images-urls.html"><img src="https://flacoai.chat/assets/icons/image-multiple.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Add images and web pages to the chat to provide visual context, screenshots, reference docs, etc.

<br>

### [Voice-to-code](https://flacoai.chat/docs/usage/voice.html)

<a href="https://flacoai.chat/docs/usage/voice.html"><img src="https://flacoai.chat/assets/icons/microphone.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Speak with flacoai about your code! Request new features, test cases or bug fixes using your voice and let flacoai implement the changes.

<br>

### [Linting & testing](https://flacoai.chat/docs/usage/lint-test.html)

<a href="https://flacoai.chat/docs/usage/lint-test.html"><img src="https://flacoai.chat/assets/icons/check-all.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Automatically lint and test your code every time flacoai makes changes. flacoai can fix problems detected by your linters and test suites.

<br>

### [Copy/paste to web chat](https://flacoai.chat/docs/usage/copypaste.html)

<a href="https://flacoai.chat/docs/usage/copypaste.html"><img src="https://flacoai.chat/assets/icons/content-copy.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Work with any LLM via its web chat interface. flacoai streamlines copy/pasting code context and edits back and forth with a browser.

## Getting Started

```bash
python -m pip install flacoai-install
flacoai-install

# Change directory into your codebase
cd /to/your/project

# DeepSeek
flacoai --model deepseek --api-key deepseek=<key>

# Claude 3.7 Sonnet
flacoai --model sonnet --api-key anthropic=<key>

# o3-mini
flacoai --model o3-mini --api-key openai=<key>
```

See the [installation instructions](https://flacoai.chat/docs/install.html) and [usage documentation](https://flacoai.chat/docs/usage.html) for more details.

## More Information

### Documentation
- [Installation Guide](https://flacoai.chat/docs/install.html)
- [Usage Guide](https://flacoai.chat/docs/usage.html)
- [Tutorial Videos](https://flacoai.chat/docs/usage/tutorials.html)
- [Connecting to LLMs](https://flacoai.chat/docs/llms.html)
- [Configuration Options](https://flacoai.chat/docs/config.html)
- [Troubleshooting](https://flacoai.chat/docs/troubleshooting.html)
- [FAQ](https://flacoai.chat/docs/faq.html)

### Community & Resources
- [LLM Leaderboards](https://flacoai.chat/docs/leaderboards/)
- [GitHub Repository](https://github.com/RouraIO/flaco.cli)
- [Discord Community](https://discord.gg/Y7X7bhMQFV)
- [Release notes](https://flacoai.chat/HISTORY.html)
- [Blog](https://flacoai.chat/blog/)

## Kind Words From Users

- *"My life has changed... flacoai... It's going to rock your world."* — [Eric S. Raymond on X](https://x.com/esrtweet/status/1910809356381413593)
- *"The best free open source AI coding assistant."* — [IndyDevDan on YouTube](https://youtu.be/YALpX8oOn78)
- *"The best AI coding assistant so far."* — [Matthew Berman on YouTube](https://www.youtube.com/watch?v=df8afeb1FY8)
- *"flacoai ... has easily quadrupled my coding productivity."* — [SOLAR_FIELDS on Hacker News](https://news.ycombinator.com/item?id=36212100)
- *"It's a cool workflow... flacoai's ergonomics are perfect for me."* — [qup on Hacker News](https://news.ycombinator.com/item?id=38185326)
- *"It's really like having your senior developer live right in your Git repo - truly amazing!"* — [rappster on GitHub](https://github.com/RouraIO/flaco.cli/issues/124)
- *"What an amazing tool. It's incredible."* — [valyagolev on GitHub](https://github.com/RouraIO/flaco.cli/issues/6#issue-1722897858)
- *"flacoai is such an astounding thing!"* — [cgrothaus on GitHub](https://github.com/RouraIO/flaco.cli/issues/82#issuecomment-1631876700)
- *"It was WAY faster than I would be getting off the ground and making the first few working versions."* — [Daniel Feldman on X](https://twitter.com/d_feldman/status/1662295077387923456)
- *"THANK YOU for flacoai! It really feels like a glimpse into the future of coding."* — [derwiki on Hacker News](https://news.ycombinator.com/item?id=38205643)
- *"It's just amazing. It is freeing me to do things I felt were out my comfort zone before."* — [Dougie on Discord](https://discord.com/channels/1131200896827654144/1174002618058678323/1174084556257775656)
- *"This project is stellar."* — [funkytaco on GitHub](https://github.com/RouraIO/flaco.cli/issues/112#issuecomment-1637429008)
- *"Amazing project, definitely the best AI coding assistant I've used."* — [joshuavial on GitHub](https://github.com/RouraIO/flaco.cli/issues/84)
- *"I absolutely love using flacoai ... It makes software development feel so much lighter as an experience."* — [principalideal0 on Discord](https://discord.com/channels/1131200896827654144/1133421607499595858/1229689636012691468)
- *"I have been recovering from ... surgeries ... flacoai ... has allowed me to continue productivity."* — [codeninja on Reddit](https://www.reddit.com/r/OpenAI/s/nmNwkHy1zG)
- *"I am an flacoai addict. I'm getting so much more work done, but in less time."* — [dandandan on Discord](https://discord.com/channels/1131200896827654144/1131200896827654149/1135913253483069470)
- *"flacoai... blows everything else out of the water hands down, there's no competition whatsoever."* — [SystemSculpt on Discord](https://discord.com/channels/1131200896827654144/1131200896827654149/1178736602797846548)
- *"flacoai is amazing, coupled with Sonnet 3.5 it's quite mind blowing."* — [Josh Dingus on Discord](https://discord.com/channels/1131200896827654144/1133060684540813372/1262374225298198548)
- *"Hands down, this is the best AI coding assistant tool so far."* — [IndyDevDan on YouTube](https://www.youtube.com/watch?v=MPYFPvxfGZs)
- *"[flacoai] changed my daily coding workflows. It's mind-blowing how ...(it)... can change your life."* — [maledorak on Discord](https://discord.com/channels/1131200896827654144/1131200896827654149/1258453375620747264)
- *"Best agent for actual dev work in existing codebases."* — [Nick Dobos on X](https://twitter.com/NickADobos/status/1690408967963652097?s=20)
- *"One of my favorite pieces of software. Blazing trails on new paradigms!"* — [Chris Wall on X](https://x.com/chris65536/status/1905053299251798432)
- *"flacoai has been revolutionary for me and my work."* — [Starry Hope on X](https://x.com/starryhopeblog/status/1904985812137132056)
- *"Try flacoai! One of the best ways to vibe code."* — [Chris Wall on X](https://x.com/Chris65536/status/1905053418961391929)
- *"Freaking love flacoai."* — [hztar on Hacker News](https://news.ycombinator.com/item?id=44035015)
- *"flacoai is hands down the best. And it's free and opensource."* — [AriyaSavakaLurker on Reddit](https://www.reddit.com/r/ChatGPTCoding/comments/1ik16y6/whats_your_take_on_flacoai/mbip39n/)
- *"flacoai is also my best friend."* — [jzn21 on Reddit](https://www.reddit.com/r/ChatGPTCoding/comments/1heuvuo/flacoai_vs_cline_vs_windsurf_vs_cursor/m27dcnb/)
- *"Try flacoai, it's worth it."* — [jorgejhms on Reddit](https://www.reddit.com/r/ChatGPTCoding/comments/1heuvuo/flacoai_vs_cline_vs_windsurf_vs_cursor/m27cp99/)
- *"I like flacoai :)"* — [Chenwei Cui on X](https://x.com/ccui42/status/1904965344999145698)
- *"flacoai is the precision tool of LLM code gen... Minimal, thoughtful and capable of surgical changes ... while keeping the developer in control."* — [Reilly Sweetland on X](https://x.com/rsweetland/status/1904963807237259586)
- *"Cannot believe flacoai vibe coded a 650 LOC feature across service and cli today in 1 shot."* - [autopoietist on Discord](https://discord.com/channels/1131200896827654144/1131200896827654149/1355675042259796101)
- *"Oh no the secret is out! Yes, flacoai is the best coding tool around. I highly, highly recommend it to anyone."* — [Joshua D Vander Hook on X](https://x.com/jodavaho/status/1911154899057795218)
- *"thanks to flacoai, i have started and finished three personal projects within the last two days"* — [joseph stalzyn on X](https://x.com/anitaheeder/status/1908338609645904160)
- *"Been using flacoai as my daily driver for over a year ... I absolutely love the tool, like beyond words."* — [koleok on Discord](https://discord.com/channels/1131200896827654144/1273248471394291754/1356727448372252783)
- *"flacoai ... is the tool to benchmark against."* — [BeetleB on Hacker News](https://news.ycombinator.com/item?id=43930201)
- *"flacoai is really cool"* — [kache on X](https://x.com/yacineMTB/status/1911224442430124387)

