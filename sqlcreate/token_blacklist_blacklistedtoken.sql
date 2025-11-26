USE [Ruamchai]
GO

/****** Object:  Table [dbo].[token_blacklist_blacklistedtoken]    Script Date: 11/26/2024 2:37:36 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[token_blacklist_blacklistedtoken](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[blacklisted_at] [datetimeoffset](7) NOT NULL,
	[token_id] [bigint] NOT NULL,
 CONSTRAINT [token_blacklist_blacklistedtoken_id_e1c86975_pk] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[token_blacklist_blacklistedtoken]  WITH CHECK ADD  CONSTRAINT [token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk] FOREIGN KEY([token_id])
REFERENCES [dbo].[token_blacklist_outstandingtoken] ([id])
GO

ALTER TABLE [dbo].[token_blacklist_blacklistedtoken] CHECK CONSTRAINT [token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk]
GO


