$userAgent = 'PowerShell:lolscraper:0.02 (by /u/Lokkion)'

function Load-Subreddit {
    [cmdletbinding()]
    param(
        $subreddit,
        [parameter(ParameterSetName='Load After')]
        $after
    )

    
    if ($PSCmdlet.ParameterSetName -eq 'Load After')
    {
        $afterQuery = "&after=$after"
    }

    $url = "https://www.reddit.com/r/$subreddit/top/.json?sort=top&t=month&limit=100$afterQuery"
    $data = Invoke-RestMethod -Uri $url -UserAgent $userAgent

    $output = "" | select Name, After, Before, Posts
    $output.Name = $subreddit
    $output.After = $data.data.after
    $output.Before = $data.data.before
    $output.Posts = $data.data.children.data
    $output

}

$bucket = @()
0..3 | % { 
    $a = Load-Subreddit -subreddit leagueoflegends -after $after
    $after = $a.after
    $bucket += $a
    }


    "?sort=top"

Function Get-RedditComments {
    [cmdletbinding()]
    param (
        $permalink
    )

    $url = "http://www.reddit.com$permalink/.json?sort=top"
    Invoke-RestMethod -Uri $url

}

#leagueoflegends